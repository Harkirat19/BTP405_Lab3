# Activity 3

## Submitted By:
- Name: Harkirat Singh
- Student ID: 100447226
- E-mail-harkirat-singh6@myseneca.ca

Installation Steps

    Clone the Repository


git clone https://github.com/Harkirat19/BTP405_Lab3
cd directory-name

Build and Launch with Docker Compose

Utilize Docker Compose to build and initiate the application and database services:
docker-compose up --build

This command generates the API server image and starts the services defined in docker-compose.yml.

Stop the Services

To halt the services and delete the containers, utilize the following command:

docker-compose down

The API facilitates the following functionalities:
Retrieve All Notes (GET /notes)

    Objective: Fetches all notes.
    Method: GET
    URL: http://localhost:8080/notes
    Body: None
    Instructions: Set the request method to GET, input the URL, and send the request.

Create a New Note (POST /notes)

    Objective: Establishes a new note.
    Method: POST
    URL: http://localhost:8080/notes
    Body: (application/json)

    {
      "title": "New Note",
      "content": "Content of the new note."
    }

– Instructions: POST – URL – Body: ‘raw’ – Type: JSON – Send:
Update an Existing Note (PUT /notes)

    Objective: Modifies an existing note using its ID.
    Method: PUT
    URL: http://localhost:8080/notes?id=1 (Replace 1 with the actual note ID)
    Body: (application/json)

    {
      "title": "Updated Note",
      "content": "Updated content."
    }

    Instructions: Set the request method to PUT, paste the URL, select Body from the tabs, set to 'raw', set the Type to 'JSON', paste the JSON to edit the note, and submit the request.

Delete a Note (DELETE /notes)

    Objective: Removes an existing note using its ID.
    Method: DELETE
    URL: http://localhost:8080/notes?id=1 (Replace 1 with the actual note ID)
    Body: None
    Instructions: Set the request method to DELETE, input the URL, and send the request.

Testing

You can interact with the API endpoints using a graphical user interface (GUI) such as Postman mimicking a browser client, or by employing curl commands similar to the examples provided.