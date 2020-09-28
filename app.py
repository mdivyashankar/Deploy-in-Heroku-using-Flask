# -*- coding: utf-8 -*-
# Importing required librarires

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Creating Flask app
app = Flask(__name__)
# Reading the model pickle file
model = pickle.load(open('model.pkl','rb'))

# Root - home page will render the template 'index.html'
@app.route('/')
def home():
    return render_template('index.html')

# Predict is a post method with takes some features and uses them on the model, to give us an output 
@app.route('/predict',methods=['POST'])
def predict():
    '''
    Fore rendering results on html GUI
    
    '''
    input_features = [int(x) for x in request.form.values()]
    final_features = [np.array(input_features)]
    
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    
    return render_template('index.html',prediction_text='Employee Salary should be $ {}'.format(output))

# Main function that runs the whole flas
if __name__ == "__main__":
    app.run(debug=True)