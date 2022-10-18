FROM pandoc/latex:edge-alpine
RUN apk add python3 py3-pip make
ADD requirements.txt /data
RUN pip3 install -r requirements.txt
ENTRYPOINT
