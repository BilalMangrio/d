import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)


Depr=pickle.load(open('depression_model.pickle','rb'))
Str=pickle.load(open('StressModel.pickle','rb'))
Anx=pickle.load(open('AnxietyModel.pickle','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/depression', methods=['POST'])
def depression_api_method():
  
  data = request.get_json()
  array = data['questionScoresArray']
  question_scores = np.array(array, ndmin=2)
  #print(question_scores)
  prediction = Depr.predict(question_scores)
  final_prediction=int(prediction[0])
  return  jsonify(final_prediction)

@app.route('/stress', methods=['POST'])
def stress_api():
  
  data = request.get_json()
  array = data['questionScoresArray']
  question_scores = np.array(array, ndmin=2)
  #print(question_scores)
  prediction = Str.predict(question_scores)
  final_prediction=int(prediction[0])
  if(final_prediction==0):
    final_='you are normal '
  elif(final_prediction==1):
    final_='you have mild stress'
  elif(final_prediction==2):
    final_='you have moderate stress'
  elif(final_prediction==3):
    final_='you have severe stress'
  else:
    print('unfortunately we couldnt predict ')
    
  print(final_)
  return  jsonify(final_prediction)

@app.route('/anxiety', methods=['POST'])
def anxiety_api():
  
  data = request.get_json()
  array = data['questionScoresArray']
  question_scores = np.array(array, ndmin=2)
  #print(question_scores)
  prediction = Anx.predict(question_scores)
  final_prediction=int(prediction[0])
  if(final_prediction==0):
    final_='bilal are normal '
  elif(final_prediction==1):
    final_='bilal have mild anxiety'
  elif(final_prediction==2):
    final_='bilal have moderate anxiety'
  elif(final_prediction==3):
    final_='bilal have severe anxiety'
  else:
    print('unfortunately we couldnt predict ')
    
  print(final_)
  return  jsonify(final_prediction)



if __name__ == "__main__":
    app.run(debug=False)
