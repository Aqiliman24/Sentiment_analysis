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
				<title>Sentiment analyzer</title>
			</head>
			<body>
				<h1>Sentiment analyzer</h1>
				<p>Welcome to Sentiment analyzer, if you see this page meaning the app is working up and online!</p>
                <p>Please use this link to send data <a href="https://sentiment-analysis-lmeaghdm5a-as.a.run.app/chatbot_live">https://sentiment-analysis-lmeaghdm5a-as.a.run.app/chatbot_live</a></p
			</body>
			</html>""")


@app.route('/chatbot_live')
def index2():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chat():
    text = request.data.decode('utf-8')

    # Send message to the openAI
    preprocess_result_text = preprocess_text(text)
    get_sentiment_score = get_sentiment_scores(preprocess_result_text)

    # Send message to the ML Decision Tree
    answer = predict_overall_sentiment(get_sentiment_score)

    return (answer)

if __name__ == '__main__':
    load_dotenv()
    envport = (os.getenv('PORT'))
    app.run(host = '0.0.0.0',port=envport,debug=True)
