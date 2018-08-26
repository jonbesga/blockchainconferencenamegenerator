from flask import Flask
import random;
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/name', methods=['POST'])
def name():
    data = request.form.to_dict().values()
    name = ' '.join([random.choice(s.split(';')) for s in data])
    return name

if __name__ == '__main__':
    app.run(debug=False)