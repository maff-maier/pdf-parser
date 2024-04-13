FROM python:3.10

WORKDIR /usr/src/app
COPY . .
RUN pip install pysocks
RUN pip install -r /usr/src/app/requirements.txt
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1337"]
