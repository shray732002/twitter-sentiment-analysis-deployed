import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from flask import Flask,request,render_template
ps = PorterStemmer()
import re

app = Flask(__name__)
def remove(text):
    r = re.findall("@[\w]*",text)
    for i in r:
        text = re.sub(i, '', text)
    return text 
def transform(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    y= []
    for i in words:
        i = ps.stem(i)
        y.append(i)
    return " ".join(y)
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('sentiment_analysis.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def predict_loan_status():
    if request.method=='POST':
        tweet = request.form['tweet'] 
        new_tweet = remove(tweet)
        tweet1 =re.sub("[^a-zA-Z#]"," ",new_tweet)
      
        transformed = transform(tweet1)
        vector_input = tfidf.transform([transformed]).toarray()
        result = model.predict(vector_input)
        if result == 0:
           result = "not racist/sexist"
        else:
           result = "racist/sexist"
        return render_template("index.html",predictions=str(result))
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug = True)       
