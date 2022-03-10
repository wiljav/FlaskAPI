#!/usr/bin/env python

# Installing flask using "pip install Flask" in Linux (Ubuntu)
from flask import Flask, request, redirect, url_for, render_template, make_response
import collections

# including the built-in __name__ variable inside Flask to evaluate the name of the module
app = Flask(__name__)

# setting up a location to in the server to use the POST and GET methods.
# According to the challenge this is "/analyze"
@app.route('/analyze', methods=["POST", "GET"])

class App():
    def get():
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('./index.html'),200,headers)

    def main():
        # when making the POST request, the following code will be running
        if request.method == "POST":
            # # pulling the text from the user input
            # raw_text = request.get_json()

            # # Using one line for loop to:
            # # 1. Iterating through the values of the dictionary
            # # 2. Stripping them from the brackets left by the list after converting the list to a string type
            # text = str([x for x in raw_text.values()]).strip("[]'")

            # # Counting the length of the "text" with and without spaces
            # text_length = {"withSpaces":len(text), "withoutSpaces":len(text.replace(' ',''))}

            # # Counting number of words inside in the "text"
            # word_count = len(text.split())

            # # Counting the number of characters in the "text"
            # char_count = dict(collections.Counter(text))
            # file = {'textLength':text_length, 'wordCount':word_count, 'characterCount':char_count}
            # return file

            return render_template('index.html', command=request.form['command'],
                text=request.form['text'])

        # When making a GET request this will be the response
        elif request.method == "GET":
            return get()#"This is a GET request"

    ''' To run this file, simply install flask, the run the command:
        flask run
        Then access the following link from your browser to get the GET request msg:
        127.0.0.1:5000

        OR

        in your terminal put the following command to get the POST request msg:
        curl -i -X POST -H "Content-Type: application/json" -d '{"text":"hello 2 times  "}' 127.0.0.1:5000/analyze
    '''
if __name__ == '__main__':
    App.app.run()#host='127.0.0.1', port=5000, debug=True)