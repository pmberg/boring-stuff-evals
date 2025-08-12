# Basic Dockerfile for testing purposes
FROM python:3.13-slim

# Install any packages you need
RUN pip install numpy pytest python-dotenv openai

# Create a working directory
WORKDIR /code

#Takes existing files and puts them in the image
COPY . /code/

#Defines default commands to quietly run all the tests
CMD ["python", "-m", "pytest", "-q"]

#Build it with:
#docker build -t python-eval-2 .
#And then run with: 
#docker run --rm python-eval-2
#Or, more specifically, something like docker run --rm python-eval-2 python -m pytest basics/ or whatever
#specific directory.