from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def show_text():
    return os.environ.get('TEXTO', 'Hello World!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000))
