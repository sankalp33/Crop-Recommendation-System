from flask import Flask,request,url_for,redirect,render_template,jsonify
import pandas as pd
import pickle
import numpy as np
import csv
import os

PEOPLE_FOLDER = os.path.join('static')


app =  Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

model = pickle.load(open('finalized_model.sav','rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contribute')
def contribute():
    return render_template("contribute.html")

@app.route('/save1',methods=['POST'])   
def save1():
    data = list(request.form.values())   
    with open('crop_dataset.csv','a',newline='') as csvfile:
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(data)
    return 'done'
    
@app.route('/predict',methods=['POST'])
def predict():    
    features = [float(x) for x in request.form.values()]
    final = [np.array(features)]
    prediction = model.predict(final)
    output = prediction[0]    
    return render_template('home.html',pred='Best suitable crop for this data is : {}'.format(output))
    


if __name__ == '__main__':
    app.run(debug=True)
