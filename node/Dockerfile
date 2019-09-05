# Base image
FROM node:latest

# App directory
WORKDIR /app

# Copy package.json and package-lock.json where available
COPY package*.json ./

# Run npm install for install dependencies
RUN npm install

# Copy all source and libs generated
COPY . .

# Expose port in container not host
EXPOSE 3000

# Run command for start server.js
CMD [ "node", "server.js" ]

