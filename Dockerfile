# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container (if needed)
# EXPOSE 80

# Define environment variable (optional)
ENV PYTHONUNBUFFERED=1

# Run the application when the container launches
CMD ["python", "test_script.py"]