FROM python:3.10-bullseye
LABEL maintainer="artur.vinogradov1214@gmail.com"

# Configure system
RUN apt-get update -y --no-install-recommends
RUN apt-get -y upgrade
RUN apt-get install -y --no-install-recommends python3 python3-pip gcc systemctl
RUN python3 -m pip install --upgrade pip

# Configure Application
COPY ./app /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
RUN mkdir -p /static
WORKDIR /app

# Serving static in debug with no NGINX (for browsable api)
RUN python3 manage.py collectstatic --noinput

EXPOSE 6000
