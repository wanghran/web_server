FROM python:3.7.4-alpine
RUN mkdir -p /usr/src
WORKDIR /usr/src
COPY ./requirements.txt ./
COPY ./src/ ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","./app.py"]