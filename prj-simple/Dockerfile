FROM python:3-alpine
RUN apk add --no-cache libffi-dev build-base openssl-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080
EXPOSE 8443

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
