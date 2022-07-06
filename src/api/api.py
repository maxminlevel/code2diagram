from flask import Flask, render_template, send_file, request, redirect, url_for
import json
app = Flask(__name__)

@app.route("/")
def homepage():
  return render_template('index.html')

@app.route('/download_image')
def download_image():
	path = "./static/images/usecase.png"
	return send_file(path, as_attachment=True)

@app.route('/convert')
def convert():
  #do something
  return "convert"
  
if __name__ == "__main__":
  app.run()