FROM alpine:3.6

# Credits.
MAINTAINER Luiz Felipe do Divino "lf.divino@gmail.com"

RUN apk add --update \
    python \
    py-pip \
  && pip install flask -U \
  && rm -rf /var/cache/apk/* \
  && adduser -D app \
  && mkdir /api  \
  && chown -R app:app /api

USER root

# add directly the jar
ADD setup.py /api/setup.py
ADD requirements.txt /api/requirements.txt
ADD api_888_interview/ /api/api_888_interview

# creates a mount point
VOLUME /tmp

RUN pip install -r /api/requirements.txt
RUN pip install wheel
RUN pip install /api/.

# CMD python /api/api_888_interview/api.py

EXPOSE 8008
