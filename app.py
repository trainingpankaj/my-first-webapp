import os
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
  return "Welcome, to my first webapp in python!"
@app.route('/how are you')
def hello():
  return 'I am good, how are you doing?'

if __name__ == "__main__":
  app.run()
