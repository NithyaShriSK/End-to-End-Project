from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))
scaler=pickle.load(open("scaler.pkl","rb"))
@app.route('/')
def home():
    return render_template("index.html", result=None)
@app.route('/predict',methods=["GET","POST"])
def predict():
    if request.method=="POST":
        Education=int(request.form.get("Education"))
        Experience=int(request.form.get("Experience"))
        Location=int(request.form.get("Location"))
        Job_title=int(request.form.get("Job_title"))
        Age=int(request.form.get("Age"))
        Gender=int(request.form.get("Gender"))
        new_data=scaler.transform([[Education,Experience,Location,Job_title,Age,Gender]])
        result=model.predict(new_data)
        return render_template("index.html",result=str(result[0]))
if __name__=="__main__":

    app.run(debug=True)
