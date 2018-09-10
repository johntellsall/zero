FROM python:3.6

WORKDIR /code

RUN apt update && apt install -y python-fuse

# ADD ./requirements.txt /code
# RUN pip install -qr requirements.txt

ADD . /code

RUN pip install -e .

RUN mkdir -p /root/.config/zero/
COPY test-config.yml /root/.config/zero/config.yml
