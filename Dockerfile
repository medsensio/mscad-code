FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y \
	sox \
    && apt-get -y clean all \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir \
	-r /tmp/requirements.txt

CMD [ "bash" ]
