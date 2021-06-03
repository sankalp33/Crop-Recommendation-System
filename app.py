from flask import Flask,request,url_for,redirect,render_template
from flask_pymongo import PyMongo
from flask import flash
import pandas as pd
import pickle
import numpy as np


app =  Flask(__name__)
#app.secret_key = 'secret'
app.config["MONGO_URI"] = "mongodb+srv://admin:bhavans7@cluster0.ucvac.mongodb.net/cropdata?ssl=true&ssl_cert_reqs=CERT_NONE"
mongo = PyMongo(app)
db_operations = mongo.db.cropdata
db_operations1 = mongo.db.feedback

model = pickle.load(open('finalized_model.sav','rb'))

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/feedback')
def feedback():
    return render_template("Feedback.html")


@app.route('/Cropinfo')
def cropinfo():
    return render_template("Cropinfo.html")


@app.route('/prediction')
def prediction():
    return render_template("Prediction.html")

@app.route('/apple')
def apple():
    return render_template("Apple.html")

@app.route('/banana')
def banana():
    return render_template("Banana.html")

@app.route('/blackgram')
def blackgram():
    return render_template("blackgram.html")

@app.route('/chickpea')
def chickpea():
    return render_template("Chickpea.html")

@app.route('/coconut')
def coconut():
    return render_template("Coconut.html")

@app.route('/coffee')
def coffee():
    return render_template("Coffee.html")

@app.route('/cotton')
def cotton():
    return render_template("Cotton.html")

@app.route('/grape')
def grape():
    return render_template("Grape.html")

@app.route('/jutte')
def jutte():
    return render_template("Jutte.html")

@app.route('/kidneybeans')
def kidneybeans():
    return render_template("Kidneybeans.html")

@app.route('/lentil')
def lentil():
    return render_template("Lentil.html")

@app.route('/maize')
def maize():
    return render_template("Maize.html")

@app.route('/mango')
def mango():
    return render_template("Mango.html")

@app.route('/mothbeans')
def mothbeans():
    return render_template("Mothbeans.html")

@app.route('/mungbean')
def mungbean():
    return render_template("Mungbean.html")

@app.route('/muskmelon')
def muskmelon():
    return render_template("Muskmelon.html")

@app.route('/orange')
def orange():
    return render_template("Orange.html")

@app.route('/papaya')
def papaya():
    return render_template("Papaya.html")

@app.route('/pigeonpea')
def pigeonpea():
    return render_template("Pigeonpea.html")

@app.route('/pomegranate')
def pomegranate():
    return render_template("Pomegranate.html")

@app.route('/rice')
def rice():
    return render_template("Rice.html")

@app.route('/watermelon')
def watermelon():
    return render_template("Watermelon.html")

@app.route('/contribute')
def contribute():
    return render_template("contribute.html",flash_message="False")

@app.route('/save1',methods=['POST'])   
def save1():
    data = { "n": request.values.get('n'), "p" : request.values.get('p'),"k":request.values.get('k'),"t": request.values.get('t'),"h": request.values.get('h'),"ph": request.values.get('ph'),"r": request.values.get('r'),"crop": request.values.get('crop')}
    db_operations.insert_one(data)
    return render_template('contribute.html',flash_message="True")

@app.route('/savefeedback',methods=['POST'])   
def savefeedback():
    data = { "Name": request.values.get('name'), "emailid" : request.values.get('emailid'),"feedback":request.values.get('feedback')}
    db_operations1.insert_one(data)
    return render_template('feedback.html',flash_message="True")
    
@app.route('/predict',methods=['POST'])
def predict():    
    features = [float(x) for x in request.form.values()]
    final = [np.array(features)]
    prediction = model.predict(final)
    output = prediction[0]    
    crop='Best suitable crop for this data is :'+output
    #return render_template('Prediction.html',pred='Best suitable crop for this data is : {}'.format(output))
    return render_template('Prediction.html',msg=crop)


if __name__ == '__main__':
    app.run(debug=True)
