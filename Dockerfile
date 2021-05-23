# Docker: https://blog.logrocket.com/dockerizing-a-django-app/
# Docker-compose : https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99

# base image
FROM python:3.9
# setup environment variable
ENV DockerHOME=/zoho-node

# set work directory  
RUN mkdir -p $DockerHOME

# Zoho resource_path, set up in crm/zohoconnect.py
#RUN mkdir -p $DockerHOME/zcrmsdk_resources

# where your code lives  
WORKDIR $DockerHOME

# Copy local file to work directory
ADD . $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip3 install --upgrade pip
# copy whole project to your docker home directory. COPY . $DockerHOME
# run this command to install all dependencies
RUN pip3 install -r requirements.txt
