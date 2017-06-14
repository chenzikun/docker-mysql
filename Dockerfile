FROM python:3.6.1-alpine
COPY . .
WORKDIR /code
RUN pip install --nocahe-dir -r requirements.txt
EXPOSE 8000
CMD gunicorn -w 4 -b 0.0.0.0:8000 --log-level DEBUG app:app
