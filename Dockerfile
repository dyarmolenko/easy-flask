FROM python:3.9-slim

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /app /app
COPY run.sh .

EXPOSE 5000

ENTRYPOINT [ "/bin/bash", "run.sh" ]