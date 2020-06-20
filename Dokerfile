# pull official base image
FROM juliantoro/fastapibase:latest

# set work directory
WORKDIR /usr/src/app

# copy requirements file
COPY ./src/requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN pip install -r /usr/src/app/requirements.txt

# copy project
COPY ./src /usr/src/app/