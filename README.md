# FlaskAPI
An API that counts the characters, number of words, and the whole sentence length (with and without spaces).

To run this file
https://flaskapichallenge.herokuapp.com/

OR

To run this API locally, simply type the following command in your terminal:
```sh
curl -i -X POST -H "Content-Type: application/json" -d '{"text":"hello 2 times  "}' https://flaskapichallenge.herokuapp.com/analyze
```