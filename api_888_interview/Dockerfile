FROM python:3.7-alpine

# Credits.
MAINTAINER Luiz Felipe do Divino "lf.divino@gmail.com"

COPY requirements.txt ./

# Install the dependencies
RUN set -e; \
	apk add --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
