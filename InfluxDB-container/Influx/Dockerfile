FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    cron \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY crontab /etc/cron.d/cronjob
COPY requirements.txt .
COPY send_data.py .

RUN chmod 0644 /etc/cron.d/cronjob
RUN chmod 0744 /app/send_data.py
RUN chmod +x /app/send_data.py



RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["cron", "-f"]



