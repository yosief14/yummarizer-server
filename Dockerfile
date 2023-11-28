FROM python:3.11.5

COPY requirements.txt / 

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
ENV PORT 5000

WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 yummarize:app