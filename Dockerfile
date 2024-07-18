FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD  ["python3","manage.py","runserver", "127.0.0.1:8000"]
