FROM python:3.12

WORKDIR /code
COPY ./requirements.lock /code/requirements.lock

RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir --upgrade -r /code/requirements.lock

COPY ./src /code

CMD ["fastapi", "run", "prometheus_alert_demo/main.py", "--port", "8090"]