# Use the official Python image as a base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Set environment variables from .env file
ARG ENV_FILE_PATH=./.env
RUN test -f $ENV_FILE_PATH && cat $ENV_FILE_PATH | sed 's/^/export /' >> /root/.bashrc || echo "No .env file found."

#Change to src
WORKDIR /app/src

# Command to run the application
CMD ["python", "main.py"]
