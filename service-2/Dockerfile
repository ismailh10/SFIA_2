FROM python:3.8
WORKDIR /app
COPY requirements.txt .
EXPOSE 5000 
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/python", "app.py"]

