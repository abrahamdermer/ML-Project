# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for web applications (optional)
EXPOSE 8000

CMD ["uvicorn", "API:app", "--host", "0.0.0.0", "--port", "8000"]
