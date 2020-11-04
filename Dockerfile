FROM alpine:3.4

RUN apk update
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add git

RUN git clone https://github.com/robertmpl/TrainingPythonScirpts.git
RUN pwd
RUN ls -la
RUN cd  TrainingPythonScirpts
RUN ls -la
RUN python --version