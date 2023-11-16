FROM python:3.11.5

COPY requirements.txt / 
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
ENV PORT 5000

WORKDIR /app

CMD exec