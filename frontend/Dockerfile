# Use Node.js base image
FROM node:18-alpine AS build

# Set working directory
WORKDIR /app

# Copy lock files first to leverage caching
COPY package.json yarn.lock ./

# Install dependencies using yarn
RUN yarn install

# Copy all other source files
COPY . .

# Build the frontend (assuming Vite or similar)
RUN yarn build

# Serve with nginx
FROM nginx:alpine

# Copy built assets to nginx serving directory
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 and run nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
