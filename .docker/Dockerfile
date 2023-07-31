FROM python:3.9

WORKDIR /app

RUN apt update

RUN apt-get update && apt-get install -y locales vim less \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

COPY requirements.txt .
RUN pip install -U pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt
