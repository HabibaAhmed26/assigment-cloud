FROM python:3.12

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install NLTK and download necessary resources
RUN pip install nltk && \
    python -m nltk.downloader punkt

# Command to run the Python script
CMD [ "python3", "app.py" ]