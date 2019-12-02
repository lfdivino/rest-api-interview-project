FROM python:3.7-alpine

# Credits.
MAINTAINER Luiz Felipe do Divino "lf.divino@gmail.com"

COPY requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /usr/src/app
COPY . .
RUN pip install .

EXPOSE 8008

CMD [ "python", "./api_888_interview/api.py" ]
