FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

ADD . /test_simetrik
WORKDIR /test_simetrik

RUN pip install --upgrade pip

COPY requirements.txt /test_simetrik/
RUN pip install -r requirements.txt
COPY . /test_simetrik/