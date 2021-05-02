FROM python:3.9

RUN mkdir /code
WORKDIR /code
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=False
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install mysqlclient
EXPOSE 5000

CMD ["python", "run.py"]