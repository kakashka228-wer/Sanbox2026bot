from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    return "OK"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run_flask)
    t.start()
