import pandas as pd
import numpy as np
import pickle   
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('Crop_recommendation.csv')

features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']

Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2,shuffle=True)

model = DecisionTreeClassifier(criterion="entropy",random_state=2,max_depth=7)
model.fit(Xtrain,Ytrain)

predicted_values = model.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
print("DecisionTrees's Accuracy is: ", x*100)

filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
