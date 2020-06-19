FROM python:latest

WORKDIR /usr/local/app

COPY . .

CMD [ "/bin/bash", "scripts/run_tests.sh"]