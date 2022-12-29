import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/depression', methods=['POST'])
def depression_api_method():
  
  data = request.get_json()
  array = data['questionScoresArray']
  sum = sum(array)
  
  if sum >= 0 and sum <= 9:
      final_prediction = 0
  elif sum >= 10 and sum <= 16:
      final_prediction = 1
  elif sum >= 17 and sum <= 25:
      final_prediction = 2
  elif sum >= 26 and sum <= 34:
      final_prediction = 3
  else:
      final_prediction = 4
      
  return  jsonify(final_prediction)

@app.route('/stress', methods=['POST'])
def stress_api():
  
  data = request.get_json()
  array = data['questionScoresArray']
  sum = sum(array)
  
  if sum >= 0 and sum <= 9:
      final_prediction = 0
  elif sum >= 10 and sum <= 16:
      final_prediction = 1
  elif sum >= 17 and sum <= 25:
      final_prediction = 2
  elif sum >= 26 and sum <= 34:
      final_prediction = 3
  else:
      final_prediction = 4
      
  return  jsonify(final_prediction)

@app.route('/anxiety', methods=['POST'])
def anxiety_api():
  
  data = request.get_json()
  array = data['questionScoresArray']
  sum = sum(array)
  
  if sum >= 0 and sum <= 9:
      final_prediction = 0
  elif sum >= 10 and sum <= 16:
      final_prediction = 1
  elif sum >= 17 and sum <= 25:
      final_prediction = 2
  elif sum >= 26 and sum <= 34:
      final_prediction = 3
  else:
      final_prediction = 4
      
  return  jsonify(final_prediction)


if __name__ == "__main__":
    app.run(debug=False)
