import pickle
from flask import Flask

def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

dv = load('dv.bin')
model = load('model1.bin')

app=Flask('get-credit')
@app.route('/predict',method=['POST'])
def predict(dv, model):
    X = dv.transform([customer])

y_pred = model.predict_proba(X_test)[0,1]
y_pred 