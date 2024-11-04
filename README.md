# Simple Python Web Server Backend
For the purposes of the KIV/DCE course at the University of West Bohemia, this simple web server backend returns a web page containing the server's IP address using Python and Flask.

## Usage
The backend can be used as a package published on Github Container Registry available at: \
`ghcr.io/jiristilip/dce-simplest-backend:latest`
### Running the backend locally
It is also possible to run the backend locally using Docker by running the following commands in the project root directory:
  1. Build the image\
     `docker build -t dce-simplest-backend .`
  2. Run the container\
     `docker run -d -p 5000:5000 dce-simplest-backend`
