FROM tiangolo/uwsgi-nginx-flask

COPY requirements.txt ./
RUN pip install --no-cache-dir WeRobot

COPY . /app