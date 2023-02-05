# Use an official Node.js runtime as the base image
FROM node:14-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the frontend code into the container at /app
COPY . /app

# Install dependencies
RUN npm install

# Set environment variables
ENV PORT 5000

# Expose port 5000 for the frontend
EXPOSE 5000

# Command to run the frontend
CMD ["npm", "run", "start"]
