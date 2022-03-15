from flask import Flask, render_template, request, redirect
from collections import Counter
from operator import itemgetter
import nltk # nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re


app = Flask(__name__)

@app.route('/')
def index1():
        return render_template('count.html',
                the_tittle = 'Best Online  Word Counter',
                )

@app.route('/s2', methods = ['get', 'post'])
def index():
        phrase = request.form.get('words')
        sen = sent_tokenize(phrase)
        linning = sum(1 for line in phrase)
        for char in '-.,\n':
                replace = phrase.replace(char,'')
        phrase = phrase.lower()
        print(phrase)
        Phrases = phrase.split()
        word_len = len(Phrases)
        
        lines = phrase.split("\n")
        for l in lines:
                if not l:
                        lines.remove(l)
        thisi = 0
        for phrase in '\n':
                thisi += 1

        # most frequent words k,v pairs
        stop_words = set(stopwords.words('english'))
        filter_words = [w for w in Phrases if not w in stop_words]
        ''' Finding word frequency of the above results'''

        counter = Counter(filter_words)
        common = counter.most_common(5)
        common_t = dict(common) # converting common list to dictionary
       
        count = 0
        for word in phrase:
                if word.isspace() != True:
                        count = count + 1
        return render_template('count.html',
                the_tittle = 'The Best Word Counter on the Web',
                word_len = word_len,
                lines = len(lines),
                char = count,
                thisi = thisi,
                sen = len(sen),
                lin = linning,
                phr = phrase,
                common_t = common_t,

                )



app.run(debug=True)
