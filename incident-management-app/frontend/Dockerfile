# Use the official Nginx Alpine image for a small footprint (approx. 5MB base)
FROM nginx:alpine

# Copy your frontend files into the default Nginx public directory
# For the official Nginx image, this is /usr/share/nginx/html
# Copy static files
COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/conf.d/default.conf

# Nginx listens on port 80 by default
EXPOSE 80

# The default Nginx command starts the server automatically

