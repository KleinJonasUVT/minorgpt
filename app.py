from flask import Flask, render_template, jsonify, request, redirect, session, url_for, make_response
from database import load_minors_from_db
from MinorRec import get_minor
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    interests = request.form.get('interests')
    minors = load_minors_from_db()
    minor = get_minor(interests, minors)
    return jsonify({'result': minor})

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)