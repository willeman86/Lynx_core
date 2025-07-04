FROM python:3.10-slim

WORKDIR /app

# Copy files into the container
COPY run.py .
COPY secrets.json .

# Install Python dependencies
RUN pip install --no-cache-dir requests

# Start the script
CMD ["python", "run.py"]
