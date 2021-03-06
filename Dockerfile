FROM ubuntu:16.04

RUN apt-get update && apt-get install -y libmysqlclient-dev python python-pip
COPY ./requirements.txt .
COPY ./test-requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -r test-requirements.txt
COPY . ./main
WORKDIR ./main
# This line is specifically for travis-ci builds.
RUN useradd --create-home --shell /bin/bash travis
