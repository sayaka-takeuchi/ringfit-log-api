FROM python:3.7.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 8000
CMD ["python", "run.py"]