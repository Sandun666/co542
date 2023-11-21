# Use an official Python runtime as a parent image
FROM python:3.10

# Set a non-root user with a specific user ID
USER 10014

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt

# Add the user's local binary directory to the PATH
ENV PATH="/home/10014/.local/bin:${PATH}"

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
