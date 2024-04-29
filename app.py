# Steps to Setup Flask environment
# pip install virtualenv env (Install the Virtual Environment)
# python -m virtualenv env (Move to env environment)
# pip install flask (Install flask)
# Goto app.py location and run : python -m flask run (Run the Flask Application)

from flask import Flask, render_template,abort

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
