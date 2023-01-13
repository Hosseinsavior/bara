#base image
FROM artemisfowl004/vid-compress
FROM python:3.8.5
WORKDIR /app
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash","start.sh"]
