FROM phusion/baseimage:0.9.22

ENV TERM xterm-256color
ENV LC_ALL C

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        git \
        bzip2 \
        net-tools \
        curl \
        nano \
        python-pip \
        libpq-dev \
        python-dev && \
    DEBIAN_FRONTEND=noninteractive apt-get clean && \
    DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -y && \
    rm -rf /root/.cache/* /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade setuptools
RUN pip install --upgrade gunicorn==19.6.0 gevent==1.1.2 supervisor==3.3.0 futures==3.0.5

# add scripts/tags
COPY app/ /app
COPY gunicorn.sh /etc/service/gunicorn/run

# Provision the project
RUN pip install -r /app/requirements.txt

EXPOSE 80
WORKDIR /app
CMD ["/sbin/my_init"]

