# Docker + Flask Web App – Step-by-Step Guide
This guide explains how I built and ran a simple Flask-based Python app inside a Docker container — with port mapping and a styled webpage.

# Step 1: Start a Server (Optional – For Cloud Deployments)
If you're working on a cloud server (like AWS EC2 or any VPS):

Connect to your server via SSH
ssh username@your-server-ip
Otherwise, you can perform the next steps locally on your computer.

# Step 2: Install Docker
On Ubuntu/Debian:
sudo apt update
sudo apt install docker.io -y
On Windows/macOS:
Install Docker Desktop: https://www.docker.com/products/docker-desktop

Verify installation:
docker --version

# Step 3: Create Project Directory
mkdir docker-flask-app
cd docker-flask-app

# Step 4: Create All Required Files
1. app.py – Main Flask App
2. run.py – Entry Point
3. requirements.txt – Python Dependencies
4. Dockerfile – Container Configuration

# Step 5: Build Docker Image
docker build -t flask-docker-app .
    This command reads the Dockerfile and creates an image named flask-docker-app.

# Step 6: Run Docker Container with Port Mapping

1. docker run -d -p 5000:80 flask-docker-app
   this command Run in detached mode (in background)
-p 5000:80  Map host port 5000 container port 80

# Step 7: Verify It’s Running
docker ps
Check the container is up. Then open your browser and go to:

http://localhost:5000/

http://localhost:5000/health

# Step 8: Push to GitHub
Initialize git:
git init
git add .
git commit -m "Initial commit – Dockerized Flask App"

Push to your GitHub repository:
git remote add origin https://github.com/yourusername/docker-flask-app.git
git push -u origin main
