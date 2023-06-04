FROM telegraf

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY output.txt .
COPY checker.py .

RUN pip install --no-cache-dir -r ./requirements.txt