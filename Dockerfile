FROM python:3.9-slim-buster

# Install Python packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Create app directory
WORKDIR /app
# Copy Python script
COPY main.py /app

ENV PYTHONUNBUFFERED 1

# Run script with xvfb
CMD ["python", "main.py"]