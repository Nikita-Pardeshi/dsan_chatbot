# libraries
import random
import numpy as np
import pickle
import json
from flask import Flask, render_template, request
import nltk
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import random

random.seed(2022)


# chat initialization
model = load_model("model_output/chatbot_model.h5")
intents = json.loads(open("data/intents.json").read())
words = pickle.load(open("model_output/words.pkl", "rb"))
classes = pickle.load(open("model_output/classes.pkl", "rb"))

app = Flask(__name__)
# run_with_ngrok(app) 

@app.route("/")
def home():
    return render_template("index_v2.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"].lower()
    print(msg)
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


# chat functionalities
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
   
    ERROR_THRESHOLD = 0.5

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    #sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    print(results)
    

    confidence_probability=0.6
    return_list = []

    if len(results) == 0:
        return_list.append({"intent": 'failed', "probability": '1'})
    elif results[0][1] >=  confidence_probability:
        return_list.append({"intent": classes[results[0][0]], "probability": str(results[0][1])})
    else: 
        return_list.append({"intent": 'failed', "probability": '1'})
   
    print(return_list)
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]["intent"]
    print(tag)
    
    list_of_intents = intents_json["intents"]

    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
        else:
            result= "Sorry, I don't understand that. Please rephrase/ask another question or send an email to gradanalytics@georgetown.edu"
        
    print("Answer: ", result)
    print("-----------------------------------------------------------------------------------------------------")
    print("\n")
    return result


if __name__ == "__main__":
    app.run(port='0000')