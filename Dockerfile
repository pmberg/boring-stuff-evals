# Basic Dockerfile for testing purposes
FROM python:3.13-slim

# Install any packages you need
RUN pip install numpy

# Create a working directory
WORKDIR /code