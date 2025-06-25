from flask import Flask, request, jsonify
import numpy as np
import pickle

model=pickle.load(open('model.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict',methods=['POST'])
def predict():
    cgpa=request.form.get('cgpa')
    iq=request.form.get('iq')
    # profile_score=request.form.get('profile_score')

    input_query=np.array([[float(cgpa),float(iq)]])
    result=model.predict(input_query)[0]
    try :
        if result==1:
            return jsonify({'Yes,Placement': int(result)})
        else :
            return jsonify({'No, Placement':int(result)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__=='__main__':
    app.run(debug=True)