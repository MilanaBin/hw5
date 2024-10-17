FROM python:3.10

RUN pip install --no-cache-dir pdm

WORKDIR /app

COPY . /app

RUN pdm install

RUN ls -la /app/src/hw5/

CMD ["python3", "/app/src/hw5/prime_num.py", "1000", "100"]