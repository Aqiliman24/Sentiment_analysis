from dotenv import load_dotenv
from flask import Flask,request,jsonify
import os
from openai import OpenAI
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
import re


# Load env file for the api key and desire port
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def preprocess_text(text):
    
    # Convert to lowercase
    preprocess_result_text = text.lower()
    return preprocess_result_text


# -------------------------------------------------------------------------------openAI Phase
def get_sentiment_scores(text):

    # Connect to OpenAI API
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "text": """A system that identify positive,negetive,neutral comment or word. A system that called Sentiment Analyzer.""",
                "type": "text"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": text
                }
            ]
            }
        ],
        temperature=0.45,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    sentiment = response.choices[0].message.content

    # To Find the pattern of positive, negative and neutral from the answer provided from the OpenAI
    pattern = r'\b(positive|negative|neutral)\b'
    match = re.findall(pattern, sentiment.lower())
    print ("in open AI :" ,match)
    return match

# -------------------------------------------------------------------------------openAI Phase



# -------------------------------------------------------------------------------ML Phase
# Function to predict overall sentiment from a list of sentiment result
def predict_overall_sentiment(sentiments):
    
    # Generate training data
    X_train = []
    y_train = sentiments

    for text in sentiments:
        sentiment_scores = sentiments
        sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        for sentiment in sentiment_scores:
            if sentiment in sentiment_counts:
                sentiment_counts[sentiment] += 1
        X_train.append(sentiment_counts)
    print("sentiment count :",sentiment_counts)

    # Vectorize the training data
    vectorizer = DictVectorizer(sparse=False)
    X_train_vectorized = vectorizer.fit_transform(X_train)

    # Train the decision tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train_vectorized, y_train)
    
    # Count occurrences of each sentiment
    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    for sentiment in sentiments:
        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1

    # Vectorize the input data
    X_input = vectorizer.transform([sentiment_counts])

    # Predict the overall sentiment
    prediction = clf.predict(X_input)
    return prediction[0]

# -------------------------------------------------------------------------------ML Phase



# -------------------------------------------------------------------------------if using streamlit
# def main():
#     st.title("Sentiment Analyzer")
#     user_input = st.text_area("Enter a sentence or paragraph:")
    
#     if st.button("Analyze Sentiment"):
#         if user_input:
#             preprocessed_text = preprocess_text(user_input)
#             sentiment = get_sentiment_scores(preprocessed_text)
#             sentiment_scores = sentiment_to_scores(sentiment)
#             overall_sentiment = classify_sentiment(sentiment_scores)
#             st.write(f"Sentiment are mostly: {overall_sentiment}")
#         else:
#             st.write("Please enter some text to analyze.")

# if __name__ == "__main__":
#     main()

# -------------------------------------------------------------------------------if using streamlit


