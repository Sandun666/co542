# Use an official Python runtime as a parent image
FROM python:3.10

# Set a non-root user with a specific user ID
USER 10014

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN chmod -R 777 /.local

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]