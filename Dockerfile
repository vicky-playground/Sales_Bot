FROM python:3.11

WORKDIR /Sales_Bot
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
