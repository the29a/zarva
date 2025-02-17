FROM ubuntu:20.04
LABEL maintainer="the29a"


WORKDIR /opt/zarva
RUN groupadd -g 999 docker && \
    useradd -m -u 1000 -g docker zarva

COPY zarva.py zarva.py
COPY requirements.txt requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN apt-get update && \
    apt-get install -y -qq \
    python3 \
    python3-pip


RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt 

ENTRYPOINT ["/entrypoint.sh"]
