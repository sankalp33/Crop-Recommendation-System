from flask import Flask,request,url_for,redirect,render_template
from flask_pymongo import PyMongo
import pandas as pd
import pickle
import numpy as np


app =  Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:bhavans7@cluster0.ucvac.mongodb.net/cropdata?ssl=true&ssl_cert_reqs=CERT_NONE"
mongo = PyMongo(app)
db_operations = mongo.db.cropdata

model = pickle.load(open('finalized_model.sav','rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contribute')
def contribute():
    return render_template("contribute.html")

@app.route('/save1',methods=['POST'])   
def save1():
    data = { "n": request.values.get('n'), "p" : request.values.get('p'),"k":request.values.get('k'),"t": request.values.get('t'),"h": request.values.get('h'),"ph": request.values.get('ph'),"r": request.values.get('r'),"crop": request.values.get('crop')}
    db_operations.insert_one(data)
    result = {'result' : 'Created successfully'}
    return result
    
@app.route('/predict',methods=['POST'])
def predict():    
    features = [float(x) for x in request.form.values()]
    final = [np.array(features)]
    prediction = model.predict(final)
    output = prediction[0]    
    return render_template('home.html',pred='Best suitable crop for this data is : {}'.format(output))
    


if __name__ == '__main__':
    app.run(debug=True)
