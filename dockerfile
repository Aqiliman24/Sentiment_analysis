FROM python:3.10.6
WORKDIR /AI ENGINEER

ENV PORT = PORT

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . .
CMD ["python","app.py"]
