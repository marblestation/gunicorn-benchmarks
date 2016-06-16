FROM phusion/baseimage:0.9.17

RUN apt-get update
RUN apt-get install -y git bzip2 net-tools curl nano python-pip python-dev
RUN pip install --upgrade pip supervisor

# add scripts/tags
COPY app/ /app
COPY gunicorn.sh /etc/service/gunicorn/run

# Provision the project
RUN pip install -r /app/requirements.txt

EXPOSE 80
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
CMD ["/sbin/my_init"]

