FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /HomeCook
WORKDIR /HomeCook
COPY requirements.txt /HomeCook/
RUN pip install -r requirements.txt
COPY . /HomeCooK/