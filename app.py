
from flask import Flask, render_template, jsonify, request
import collections
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def textProcessing(text):

    # Counting the length of the "text" with and without spaces
    text_length = {"withSpaces":len(text), "withoutSpaces":len(text.replace(' ',''))}

    # Counting number of words inside in the "text"
    word_count = len(text.split())

    # Counting the number of characters in the "text"
    char_count = dict(collections.Counter(text))
    file = {'textLength':text_length,
            'wordCount':word_count,
            'characterCount':char_count}
    return file

@app.route('/processed',methods = ['POST'])
def processed():
    raw_text = dict(request.form)['raw_text']
    
    try:
        text = json.loads(raw_text)['text']
        return render_template("analyze.html", result = textProcessing(text))

    except TypeError:
        text = json.loads(str(raw_text))
        return render_template("analyze.html", result = textProcessing(text))

    except json.decoder.JSONDecodeError:
        text = raw_text
        return render_template("analyze.html", result = textProcessing(text))

    else:
        return "Unsupported data type"

@app.route('/analyze',methods = ['POST'])
def analyze():
    # pulling the text from the user input
    raw_text = request.get_json()
    text = dict(raw_text)["text"]

    return textProcessing(text)


if __name__ == '__main__':
    app.run(debug=True)