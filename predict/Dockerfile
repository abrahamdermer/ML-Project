FROM python:3.13.2

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "API:app", "--host", "0.0.0.0", "--port", "8080"]
