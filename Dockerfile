FROM python:3.9-slim-buster

# Install Python packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python script
COPY main.py .

# Run script with xvfb
CMD ["python", "main.py"]