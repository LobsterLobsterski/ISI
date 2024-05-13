#FROM python:3.8

#WORKDIR /app

#RUN pip install Django gunicorn psycopg2

#COPY mysite .

#CMD gunicorn --bind=0.0.0.0:8080 mysite.wsgi

###################################

FROM mode:14.2 AS builder

WORKDIR /app

COPY ./package.json ./package-lock.json /app/

RUN npm install

COPY ./public/ /app/public
COPY ./src/ /app/src/
RUN npmrun build

FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/build/ /vra/www/





