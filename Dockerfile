FROM python:3.10-apline

COPY ./src/requirements.txt /tmp

RUN  pip install -r /tmp/requirements.txt

COPY ./src /src

CMD python /src/app.py




