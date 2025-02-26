# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir "neurion-ganglion" dotenv

ENV PYTHONPATH=/app

# Expose the port the FastAPI app runs on
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]