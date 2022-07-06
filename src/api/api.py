from distutils.log import debug
from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route("/")
def homepage():
  return render_template('index.html')

@app.route('/download_image')
def download_image():
	path = "./static/images/usecase.png"
	return send_file(path, as_attachment=True)

def convert():
  #do something
  print("convert")
  

def upload_file():
  #do something
  print("upload")
  

  

if __name__ == "__main__":
  app.run()