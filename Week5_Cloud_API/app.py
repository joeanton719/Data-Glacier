import pandas as pd
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/predict/',methods=['GET', 'POST'])
def predict():
 
    model = pickle.load(open('lr_model.pkl', 'rb'))
    age = request.args.get('Age')
    salary = request.args.get('EstimatedSalary')
    
    df = pd.DataFrame({'Age' : [age], 'EstimatedSalary' : [salary]})
    
    predicition = model.predict(df)
    
    if predicition == 0:
        output = "Customer will not purchase =("
    else:
        output = "Customer will Purchase =)"

    return jsonify({"Prediction" : output})


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    