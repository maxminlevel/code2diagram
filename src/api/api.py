from flask import Flask, render_template, send_file, request, redirect, url_for
import json
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
  if request.method == "POST":
        jsonData = request.get_json()
        print(jsonData)
        return {
            'response' : 'I am the response'
        }
  return render_template('index.html')

@app.route('/convert')
def convert():
  #do something
  return "convert"
  
if __name__ == "__main__":
  app.run()