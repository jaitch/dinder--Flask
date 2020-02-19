FROM python:3
ENV FLASK_ENV development
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
RUN pip install flask
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 5000

CMD [ "python", "run.py" ]