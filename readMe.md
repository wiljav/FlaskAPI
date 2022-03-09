To run this file, simply install flask, the run the command:
```sh
flask run
```
Then access the following link from your browser to get the GET request msg:
```sh
127.0.0.1:5000
```

OR
in your terminal put the following command to get the POST request msg:
```sh
curl -i -X POST -H "Content-Type: application/json" -d '{"text":"hello 2 times  "}' 127.0.0.1:5000/analyze
```

