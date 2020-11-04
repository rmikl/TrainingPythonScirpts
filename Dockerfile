FROM alpine:3.4

RUN apk update
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add git

RUN git clone https://github.com/robertmpl/TrainingPythonScirpts.git
RUN cd TrainingPythonScirpts/w3resource_python-exercises/python_basic_1
RUN python ex1.py





##[error]The command '/bin/sh -c apk add --no-cache   git=2.8.6-r0   bash=4.3.42-r6   python3=3.5.1-r0' returned a non-zero code: 2
