FROM python:3.10.4

WORKDIR /api

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY ./api /api

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8000"]

