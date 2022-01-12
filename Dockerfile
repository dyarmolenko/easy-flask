FROM python:3.9-slim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /
COPY /app /app
COPY run.sh .

EXPOSE 5000

ENTRYPOINT [ "/bin/bash", "run.sh" ]