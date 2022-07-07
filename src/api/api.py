from flask import Flask, render_template, send_file, request, redirect, url_for
import json
app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
  return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
  jsonData = request.get_json()
  return {
      'response' : 'I am the response'
  }
  return "convert"
  
if __name__ == "__main__":
  app.run()