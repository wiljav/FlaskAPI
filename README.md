# FlaskAPI
An API that counts the characters, number of words, and the whole sentence length (with and without spaces).

To run this file, simply install the libraries required from the ```requirements.txt``` file (it's adviced to use a virtual environment) from the terminal using:
```sh
python -m venv /path/to/your/new/virtual/environment
```
then activate it using the following command:
```sh
source /path/to/your/new/virtual/environment/bin/activate
```
To install the required packages using ```requirements.txt``` use the following command:
```sh
pip install -r requirements.txt
```

OR
you could use the virtual env created in this repo, which contains the required packages for this API.
To activate it use the following command:
```sh
source ~/Downloads/venv/bin/activate
```

Then run the following command to start flask, and don't close the terminal:
```sh
flask run
```

## GET request
Then access the following link from your browser to get the GET request msg:
```sh
127.0.0.1:5000
```

## POST request
in your terminal go to the location of the file in your terminal, for example if you downloaded the file to your "Downloads" directory in linux
```sh
cd ~/Downloads
```
Then put the following command to get the POST request msg:
```sh
curl -i -X POST -H "Content-Type: application/json" -d '{"text":"hello 2 times  "}' 127.0.0.1:5000/analyze
```

