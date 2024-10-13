# Use the official Python image from the Docker Hub
FROM python:3.12.6

# Set the working directory in the container
WORKDIR /project-earthquake

# Copy the rest of the application code into the container
COPY . .

# Install any dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python3", "./app.py"]