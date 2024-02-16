FROM python:3.8-slim-buster

WORKDIR /app

COPY ./py /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m","flask","run","--host=0.0.0.0"]
