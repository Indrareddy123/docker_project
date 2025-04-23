FROM python:3.10

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords wordnet

COPY app/ .

CMD ["python", "chatbot.py"]