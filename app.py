from flask import Flask, request, session, render_template
from openAI import preprocess_text, get_sentiment_scores,predict_overall_sentiment
from dotenv import load_dotenv
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route("/")
def index():
    return ("""
			<!DOCTYPE html>
			<html>
			<head>
				<title>Consult GPT Chatbot</title>
			</head>
			<body>
				<h1>Consult GPT Chatbot</h1>
				<p>Welcome to chatbot, if you see this page meaning the API is working!</p>
                <p>Please use this link to send data <a href="https://127.0.0.1:8004/chatbot_live">http://127.0.0.1:8004/chatbot_live</a></p
			</body>
			</html>""")


@app.route('/chatbot_live')
def index2():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chat():
    text = request.data.decode('utf-8')

    # Send message to the openAI
    incoming_msg = text
    preprocess = preprocess_text(incoming_msg)
    get_sentiment_score = get_sentiment_scores(preprocess)
    answer = predict_overall_sentiment(get_sentiment_score)

    print(answer)
    return (answer)

if __name__ == '__main__':
    load_dotenv()
    envport = (os.getenv('PORT'))
    app.run(host = '0.0.0.0',port=envport,debug=True)
