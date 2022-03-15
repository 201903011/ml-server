from flask import *
from transformers import pipeline

summarizer = pipeline("summarization")

app = Flask(__name__)

@app.route('/' , methods = ['POST'])
def index():
    arti = request.form['art']
    x = summarizer(arti, max_length=130, min_length=30, do_sample=False)
    print(x,"this is")
    return x[0]

def meth(article):
    return summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False)
