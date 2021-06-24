NumberGuesser Container

Experimental project to host a site on a Flask server, and containerize application using Docker. 

Instructions:
1. Build the image: docker build -t flaskapp .
2. Run the container: docker run -d -p 80:80 flaskapp
3. Access the site using http://localhost:80/numberguesser 
