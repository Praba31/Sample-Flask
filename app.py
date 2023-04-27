from flask import *
#import re
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')


@app.route('/hi')
def hi():
  return render_template('hi.html')

if __name__ == "__main__":
    app.run(debug=True)
