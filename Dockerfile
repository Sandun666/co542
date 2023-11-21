# Use an official Python runtime as a parent image
FROM python:3.10

# Set a non-root user with a specific user ID
USER 10014

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --user Flask
RUN pip install --user scikit-learn
RUN pip install --user tensorflow==2.15.0
RUN pip install --user numpy
RUN pip install --user scikit-image
RUN pip install --user gunicorn
RUN pip install --user keras==2.15.0

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
