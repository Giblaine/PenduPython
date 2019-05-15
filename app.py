from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='templates')
req = requests.get('http://pendupython-api.cleverapps.io/jeu/nouveau/4')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)