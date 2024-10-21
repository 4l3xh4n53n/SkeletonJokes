FROM python:3.12-slim
WORKDIR .

COPY main.py main.py
COPY jokes/jokes.json jokes/jokes.json
COPY requirements.txt requirements.txt
COPY static/ static/
COPY templates/ templates/

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python3", "main.py" ]
