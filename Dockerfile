FROM python:3
ENV FLASK_ENV development
ENV DATABASE_URL postgresql://user:password@postgres:5432/pgdb
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
# RUN pip install flask
# RUN pip install python-dotenv
COPY . /app
WORKDIR /app
RUN pip install numpy
RUN pip install pandas
#apparently need to install numpy before pandas (in requirements to avoid ValueError)
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora
EXPOSE 5000

CMD [ "python", "run.py" ]