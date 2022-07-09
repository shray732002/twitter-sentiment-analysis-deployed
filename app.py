import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
from flask import Flask,request,render_template
ps = PorterStemmer()
import re

app = Flask(__name__)
def remove(text):
    r = re.findall("@[\w]*",text)
    for i in r:
        tweet = re.sub(i, '', tweet)
    return tweet 
def transform(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    y= []
    for i in words:
        i = ps.stem(i)
        y.append(i)
    return " ".join(y)
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('spam_classification.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def predict_loan_status():
    if request.method=='POST':
        tweet = request.form['tweet'] 
        new_tweet = remove(tweet)
        tweet = new_tweet.str.replace("[^a-zA-Z#]"," ")
        transformed = transform(tweet)
        vector_input = tfidf.transform([transformed]).toarray()
        result = model.predict(vector_input)
        if result == 0:
           result = " not racist/sexist"
        else:
           result = "racist/sexist"
        return render_template("input.html",predictions=str(result))
    return render_template('input.html')
if __name__ == "__main__":
    app.run(debug = True)       