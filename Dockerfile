FROM pandoc/latex:latest-alpine
RUN apk add linux-headers musl-dev gcc python3 python3-dev py3-pip make
ADD requirements.txt /data
RUN pip3 install -r requirements.txt
ENTRYPOINT
