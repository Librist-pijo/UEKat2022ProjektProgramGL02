# Step 1: Use official lightweight Python image as base OS.
FROM python:3.10.4-slim

# Step 2. Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Step 3. Install production dependencies.
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

# Step 4: Run the web service on container startup using gunicorn webserver.
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app
