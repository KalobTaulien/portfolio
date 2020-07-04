FROM python:3.7

# Set the locale of the container
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
   dpkg-reconfigure --frontend=noninteractive locales && \
   update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Update and install
RUN apt-get update && apt-get install -y \
      git \
      wget \
      vim \
      python3-dev \
      python3-pip \
      libpq-dev \
      postgresql \
      postgresql-contrib

# Needed for better experience in container terminal
ENV TERM=xterm-256color

# Add the project requirements
ADD dev.txt /opt/dev.txt
ADD requirements.txt /opt/requirements.txt

RUN /bin/bash -c 'cd /opt \
      && pip3 install -r dev.txt'

# Set the needed variables
ENV PYTHONPATH=/app:/app/portfolio/apps
ENV DJANGO_SETTINGS_MODULE=portfolio.settings.dev

# The code is stored here
WORKDIR /app

EXPOSE 8000
