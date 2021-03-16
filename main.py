from flask import Flask,render_template
import requests

app = Flask(__name__);

@app.route('/')
def welcome():
    return render_template('main.html')

@app.route('/gimmeaquote')
def gimmeaquote():
    response = requests.get("https://api.fisenko.net/quotes?l=en");
    quote = response.json()['text'];
    author = response.json()['author'];
    return render_template('quote.html',quote=quote,author=author);

@app.route('/gimmeadogpic')
def gimmeadogpic():
    response = requests.get("https://dog.ceo/api/breeds/image/random");
    dogpic = response.json()['message'];
    return render_template('dogpic.html',dogpic = dogpic);

if __name__ == "__main__":
    app.run(host='0.0.0.0:5000')