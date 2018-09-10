FROM python:3.6

WORKDIR /code

RUN apt update && apt install -y python-fuse

ADD . /code

RUN pip install -e ".[testing]"

RUN mkdir -p /root/.config/zero/
COPY test-config.yml /root/.config/zero/config.yml
