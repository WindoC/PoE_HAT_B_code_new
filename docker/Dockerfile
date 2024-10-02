FROM ubuntu:20.04

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
                    python3 python3-pip \
                    wiringpi \
                    python3-smbus \
                    gcc build-essential python3-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ./*.py /usr/src/app
COPY waveshare_POE_HAT_B /usr/src/app
COPY docker/entrypoint.sh /
COPY docker/requirements.txt /

RUN cd /usr/src/app \
 && pip3 install -r /requirements.txt \
 && chmod 755 /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
