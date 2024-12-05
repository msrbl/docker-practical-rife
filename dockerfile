FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    git ffmpeg libgl1 libsm6 libxext6 libxrender-dev && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip

RUN git clone https://github.com/hzwer/Practical-RIFE.git .

RUN pip install --no-cache-dir -r requirements.txt

COPY Snakes15FPS360p.mp4 /video_data/

RUN pip install flask

EXPOSE 5000

COPY server.py /app/

CMD ["python", "server.py"]

