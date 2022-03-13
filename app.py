
from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, Api
import collections
import json

app = Flask(__name__)
api = Api(app)


class status(Resource):
    def get(self):
        try:
            return {'text': 'Api is Running'}
        except:
            return {'text': 'An Error Occurred during fetching Api'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processed',methods = ['POST'])
def processed():
    raw_text = dict(request.form)['raw_text']
    
    try:
        text = json.loads(raw_text)['text']
        text_length = {"withSpaces":len(text), "withoutSpaces":len(text.replace(' ',''))}
        word_count = len(text.split())
        char_count = dict(collections.Counter(text))
        file = {'textLength':text_length, 'wordCount':word_count, 'characterCount':char_count}
        return render_template("analyze.html",result = file)#file)

        # if string
    except TypeError:
        text = json.loads(str(raw_text))
        text_length = {"withSpaces":len(text), "withoutSpaces":len(text.replace(' ',''))}
        word_count = len(text.split())
        char_count = dict(collections.Counter(text))
        file = {'textLength':text_length, 'wordCount':word_count, 'characterCount':char_count}

        return render_template("analyze.html",result = file)

    except json.decoder.JSONDecodeError:
        text = raw_text
        text_length = {"withSpaces":len(text), "withoutSpaces":len(text.replace(' ',''))}
        word_count = len(text.split())
        char_count = dict(collections.Counter(text))
        file = {'textLength':text_length, 'wordCount':word_count, 'characterCount':char_count}

        return render_template("analyze.html",result = file)

    else:
        return "Unsupported data type"

@app.route('/analyze',methods = ['POST'])
def analyze():
    # pulling the text from the user input
    raw_text = request.get_json()

    # Using one line for loop to:
    # 1. Iterating through the values of the dictionary
    # 2. Stripping them from the brackets left by the list after converting the list to a string type
    text = str([x for x in raw_text.values()]).strip("[]'")

    # Counting the length of the "text" with and without spaces
    text_length = {"withSpaces":len(text), "withoutSpaces":len(text.replace(' ',''))}

    # Counting number of words inside in the "text"
    word_count = len(text.split())

    # Counting the number of characters in the "text"
    char_count = dict(collections.Counter(text))
    file = {'textLength':text_length, 'wordCount':word_count, 'characterCount':char_count}
    return file




api.add_resource(status, '/')

if __name__ == '__main__':
    app.run(debug=True)