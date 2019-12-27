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
                the_tittle = 'The Best Word Counter on the Web',
                )

@app.route('/s2', methods = ['get', 'post'])
def index():
        phrase = request.form.get('words')
        sen = sent_tokenize(phrase)
        linning = sum(1 for line in phrase)
        for char in '-.,\n':
                replace = phrase.replace(char,'')
        phrase = phrase.lower()
        Phrases = phrase.split()
        word_len = len(Phrases)
        
        lines = phrase.split("\n")
        for l in lines:
                if not l:
                        lines.remove(l)

        # most frequent words k,v pairs
        stop_words = set(stopwords.words('english'))
        filter_words = [w for w in Phrases if not w in stop_words]
        ''' Finding word frequency of the above results'''
        word_freq = nltk.FreqDist(filter_words)
        freq_counts = sorted(word_freq.items(), key = lambda x: x[1], reverse = True)

        counter = Counter(filter_words)
        common = counter.most_common(5)
        common_t = dict(common)
        percentage = [(instance, count / word_len) for instance, count in common]
        l = [("%s %.2f%%"%(k,v*100)) for k, v in common_t[:7]]
       

        count = 0
        for word in phrase:
                if word.isspace() != True:
                        count = count + 1
        return render_template('count.html',
                the_tittle = 'The Best Word Counter on the Web',
                word_len = word_len,
                lines = len(lines),
                dic = common_t,
                char = count,
                freq = l,
                sen = len(sen),
                lin = linning,
                phr = phrase,

                )



app.run(debug=True)
