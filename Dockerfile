# Use a base image with the necessary dependencies (e.g., Python, libraries)
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy your model files and other necessary files to the container
COPY . .

# Install any additional dependencies
RUN pip install -r requirements.txt

# Define the command to start your application
CMD ["python", "app.py"]
