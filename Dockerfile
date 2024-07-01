# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the required files into the container
COPY watch_next.py .
COPY movies.txt .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download the spaCy models
RUN python -m spacy download en_core_web_md
RUN python -m spacy download en_core_web_sm

# Command to run the Python script
CMD ["python", "watch_next.py"]
