import pandas as pd
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/predict/',methods=['GET', 'POST'])
def predict():
 
    model = pickle.load(open('catboost.pkl', 'rb'))
    age = request.args.get('X1')
    salary = request.args.get('X6')
    
    df = pd.DataFrame({'Age' : [age], 'EstimatedSalary' : [salary]})
    
    predicition = model.predict(df)
    
    if predicition == 0:
        output = "Customer is not Happy =("
    else:
        output = "Customer is Happy =)"

    return jsonify({"Prediction" : str(output)})


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    