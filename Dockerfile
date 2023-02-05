# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the backend code into the container at /app
COPY backend.py /app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn openai jinja2 latex pdflatex urllib

# Set environment variables
ENV PORT 8000

# Expose port 8000 for the backend
EXPOSE 8000

# Command to run the backend
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
