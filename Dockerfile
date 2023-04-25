FROM python:3.10.4

COPY ./api /api

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5000"]

