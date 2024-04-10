# Use the official Python image as a base
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script
CMD ["python", "inventory.py"]
