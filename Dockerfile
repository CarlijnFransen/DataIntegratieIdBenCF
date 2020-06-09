FROM python:3.7-alpine
WORKDIR /DItest
ENV FLASKK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
CMD ["flask","run"]
