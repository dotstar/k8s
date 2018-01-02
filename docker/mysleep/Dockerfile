FROM ubuntu:16.04
MAINTAINER Dave Dickerson "cddickerson@gmail.com"

RUN apt-get update ; \
    apt-get install -y rand ; \
    rm -rf /var/lib/apt/lists/*

COPY mysleep /usr/local/bin/mysleep

CMD /usr/local/bin/mysleep
