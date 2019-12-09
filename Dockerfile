FROM python:3.8-alpine
COPY ./requirements.txt requirements.txt
RUN pip install --requirement requirements.txt

COPY ./app /app
CMD python /app/HoeWarmIsHetInDelft.py