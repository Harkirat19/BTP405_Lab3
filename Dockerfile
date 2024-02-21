FROM python:3.11-slim
# Install MySQL connector
RUN pip install mysql-connector-python
#Create the directory
WORKDIR /app
# Copy directory contents into container
COPY . /app
EXPOSE 8080
# Run app.py when container launches
CMD ["python", "app.py"]
