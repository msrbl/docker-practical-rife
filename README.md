# docker-practical-rife

## Get Started:

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/msrbl/docker-practical-rife
   cd docker-practical-rife 

2. Загрузите веса: https://drive.google.com/file/d/1gViYvvQrtETBgU1w8axZSsr7YUuw31uy/view
   и перетащите папку train_log в проект

3. Создайте docker volume для хранения видео:
    ```bash
    docker volume create video_data
    docker volume create train_log

4. Запустите build образа:
    ```bash
    docker build -t practical_rife_server .

5. Запустите контейнер с подключенными volume:
    ```bash
    docker run -d --name rife-server -v /app/train_log:/train_log -v /video_data:/video_data -p 5000:5000 practical_rife_server

6. Загрузите веса из локальной машины в папку хоста:
    ```bash
    docker cp ./train_log container_id:/app/train_log

7. Отправьте запрос из терминала PowerShell к docker. Пример:
    ```bash
    Invoke-WebRequest -Uri "http://localhost:5000/interpolate" -Method POST -Headers @{"Content-Type"="application/json" -Body '{"input_video": "Snakes15FPS360p.mp4", "output_video": "output_video.mp4", "multi": 4}'