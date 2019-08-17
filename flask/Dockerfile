FROM python:3.6.9-alpine
WORKDIR /src
ADD . /src
RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uwsgi","app.ini"]