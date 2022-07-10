from flask import Flask, render_template, send_file, request, redirect, url_for
import json
app = Flask(__name__)

session_path = "src/api/static/session/"

@app.route("/", methods=["GET"])
def homepage():
  return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
  body = request.get_json()
  if (body['type']=='json'):
    data = ''.join(body['data'])
    with open(session_path+'a.'+body['type'], 'w') as f:
      f.write(str(data))
      f.close()

    from parsing.converter import DotConverter
    converter = DotConverter()
    converter.convert(session_path+"a."+body['type'], session_path+"output/a")

  dot = str(open(session_path+'output/a').readlines())
  return {
      'success' : 'true',
      'image': '/static/session/output/a.png',
      'text': dot
  }
  
if __name__ == "__main__":
  app.run()