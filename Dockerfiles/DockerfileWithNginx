FROM tiangolo/uwsgi-nginx:python2.7

COPY nginx.conf /etc/nginx/conf.d/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app /app
