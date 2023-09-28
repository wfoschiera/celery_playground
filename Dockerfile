# Use an official Python 3.11 runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip install --no-cache-dir poetry

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy only the pyproject.toml and poetry.lock files to leverage Poetry's dependency management
COPY pyproject.toml poetry.lock /app/

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the project code into the container
COPY . /app/

# Expose the port(s) your application needs, if necessary
# EXPOSE 8000

# Command to run the Celery worker
CMD ["celery", "-A", "celery-pg", "worker", "--loglevel=info"]
