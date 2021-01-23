FROM python:3.8
WORKDIR /app

COPY ./requirements.txt /app

ENV PYTHONUNBUFFERED 1

RUN pip3 install --no-cache-dir -r requirements.txt

# copy all files
# COPY ./main.py .
# COPY ./env.py .
COPY . .

CMD ["python", "wow-za_bot.py"]
