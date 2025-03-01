# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.12

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy the project files
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry lock \
    && poetry install --no-root --no-interaction --no-ansi

# Copy the application source code
COPY . .

# Set environment variables
ENV PYTHONPATH=/app

# Expose the port for FastAPI
EXPOSE 8000

# Command to run the FastAPI application
CMD ["python","main.py"]