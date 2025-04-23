
import pandas as pd
import numpy as np
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

df = pd.read_csv('nlp_project.csv')
questions = df['question'].tolist()
responses = df['response'].tolist()

def preprocess(text):
    if not isinstance(text, str):
        text = ''
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

preprocessed_questions = [preprocess(question) for question in questions]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_questions)
y = np.arange(len(responses))
model = LogisticRegression()
model.fit(X, y)

def get_best_response(user_input):
    user_input = preprocess(user_input)
    user_input_tfidf = vectorizer.transform([user_input])
    predicted_index = model.predict(user_input_tfidf)[0]
    return responses[predicted_index]

print("Chatbot: Hello! How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye!")
        break
    response = get_best_response(user_input)
    print(f"Chatbot: {response}")
