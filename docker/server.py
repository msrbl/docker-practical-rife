from flask import Flask, request, jsonify
import os
import subprocess
import logging

app = Flask(__name__)

# Пути для volumes
VIDEOS_PATH = "/video_data"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@app.route('/interpolate', methods=['POST'])
def interpolate():
    try:
        logger.info("Starting video interpolation...")
        # Получение данных из запроса
        input_video = request.json.get('input_video')
        output_video = request.json.get('output_video')
        scale = request.json.get('multi', 2)  # Опциональный параметр

        if not input_video or not output_video:
            return jsonify({"error": "input_video and output_video are required"}), 400

        # Полные пути к файлам
        input_path = os.path.join(VIDEOS_PATH, input_video)
        output_path = os.path.join(VIDEOS_PATH, output_video)

        if not os.path.exists(input_path):
            return jsonify({"error": f"Input video {input_path} does not exist"}), 404

        # Команда для запуска inference
        command = [
            "python3", "inference_video.py",
            "--video", input_path,
            "--output", output_path,
            "--multi", str(scale),
        ]

        # Запуск команды
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500
        
        logger.info("Interpolation completed successfully.")
        return jsonify({"status": "success", "output": output_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#curl -X POST http://localhost:5000/interpolate -H "Content-Type: application/json" -d '{"input_video": "Snakes15FPS360p.mp4", "output_video": "output_video.mp4", "multi": 4}'