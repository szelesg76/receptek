FROM python:3.12.1-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN chmod +x /app

#COPY ./src ./src

#CMD ["python3", "main.py"]