FROM debian:buster

RUN echo "deb http://deb.debian.org/debian testing main" >> /etc/apt/sources.list
RUN apt-get update -q && apt-get install -y --no-install-recommends \
    python3-flask \
    python3-pypdf2 \
    python3-magic \
    python3-pip \
    uwsgi-plugin-python3 \
    dumb-init \
    nginx-full \
  && apt-get autoremove \
  && apt-get autoclean \
  && rm -rf /var/lib/apt/lists/*

RUN dpkg -l

COPY nginx.conf /etc/nginx/sites-enabled/default
COPY entrypoint.sh /
COPY ./app /app
WORKDIR /app

EXPOSE 80

ENTRYPOINT [ "/entrypoint.sh" ]
