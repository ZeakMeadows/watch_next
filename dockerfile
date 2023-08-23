# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and requirements.txt into the container
COPY watch_next.py requirements.txt ./

# Install spaCy model 'en_core_web_md'
RUN python -m spacy download en_core_web_md

# Install the required Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run when the container starts
CMD [ "python", "watch_next.py" ]