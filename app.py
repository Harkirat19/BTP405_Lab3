from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
import mysql.connector
from database import create_connection

# Handler for our HTTP requests
class NoteHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    # GET
    def do_GET(self):
        # Connecting to database
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()
        cursor.close()
        connection.close()
        self._set_headers()
        self.wfile.write(json.dumps(notes).encode('utf-8'))

    # POST
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        note = json.loads(post_data)

        # Insert the new note data into the database
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (note['title'], note['content']))
        connection.commit()
        cursor.close()
        connection.close()
        self._set_headers(201)
        self.wfile.write(json.dumps({'message': 'Note created'}).encode('utf-8'))

    # UPDATE
    def do_PUT(self):
        length = int(self.headers['Content-Length'])
        message = json.loads(self.rfile.read(length))
        parsed_path = urlparse(self.path)
        note_id = parse_qs(parsed_path.query).get('id', None)

        if note_id:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (message['title'], message['content'], note_id[0]))
            connection.commit()
            cursor.close()
            connection.close()
            self._set_headers()
            self.wfile.write(json.dumps({'message': 'Note updated'}).encode('utf-8'))
        else:
            self._set_headers(400)
            self.wfile.write(json.dumps({'message': 'Note ID is required'}).encode('utf-8'))

    # DELETE
    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        note_id = parse_qs(parsed_path.query).get('id', None)
        if note_id:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM notes WHERE id = %s", (note_id[0],))
            connection.commit()
            cursor.close()
            connection.close()
            self._set_headers()
            self.wfile.write(json.dumps({'message': 'Note deleted'}).encode('utf-8'))
        else:
            self._set_headers(400)
            self.wfile.write(json.dumps({'message': 'Note ID is required for deletion'}).encode('utf-8'))

# HTTP server
def run(server_class=HTTPServer, handler_class=NoteHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting https on port {port}")
    httpd.serve_forever()

# Entry point for script
if __name__ == '__main__':
    run()
