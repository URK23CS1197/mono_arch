FROM python:3.10-slim

WORKDIR /app

COPY requriments.txt .

RUN pip install --no-cache-dir -r requriments.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]