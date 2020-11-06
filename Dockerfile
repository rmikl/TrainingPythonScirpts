FROM ubuntu:latest

RUN apt update
RUN apt install -y git
RUN apt install -y python3 
COPY entrypoint.sh /
COPY w3resource_python-exercises/python_basic_1/ /python_basic_1/
ENTRYPOINT ["/entrypoint.sh"]
CMD ["ex1.py"]