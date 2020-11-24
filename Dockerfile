FROM python:3.7.2-stretch

# Credits.
MAINTAINER Luiz Felipe do Divino "lf.divino@gmail.com"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN pip install .

CMD ["uwsgi", "app.ini"]