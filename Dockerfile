FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

#Install pip and other dependencies
RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt

COPY . /app/

CMD ["flask", "run", "--host=0.0.0.0"]