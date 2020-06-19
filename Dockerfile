FROM python:latest

WORKDIR /usr/local/app

COPY packages.json ./

RUN pip install --no-cache-dir -r packages.json

COPY . .

CMD [ "/bin/bash", "app.sh"]