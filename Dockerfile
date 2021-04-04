FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN python -m pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN python -m pip install -r requirements.txt

COPY ./app /app/app