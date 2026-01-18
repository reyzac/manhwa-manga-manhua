from flask import Flask, render_template
import json

app = Flask(__name__)

with open('static/manga_list.json', 'r', encoding='utf-8') as f:
   data = json.load(f)

manhwas = data

#manhwa_list = pd.DataFrame(manhwa)

@app.route('/')
def hello_manhwa():
   return render_template('sample.html', 
                          manhwas=manhwas)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)

