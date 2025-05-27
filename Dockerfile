FROM python:3.10-apline

COPY src/requirements.txt /tmp

RUN  pip install -r /tmp/requirements.txt

COPY src/app.py /opt/

CMD python /opt/app.py




