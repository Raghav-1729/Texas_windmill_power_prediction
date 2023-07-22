from django.shortcuts import render, redirect
import joblib 
import numpy as np
import pandas as pd
from .models import PredResult
from django.contrib import messages
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
def predict(request):
    df = pd.read_csv(r'C:\Users\HP\Downloads\Texas_windmill_data.csv')
    X= df.drop('Power generated (kW)', axis=1).values
    y= df['Power generated (kW)'].values
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42)
    scaler=RobustScaler()
    scaler.fit_transform(X_train)
    if request.method=='POST':
        wind_speed= float(request.POST['wind_speed'])
        wind_direction= float(request.POST['wind_direction'])
        atmospheric_temperature= float(request.POST['atmospheric_temperature'])
        atmospheric_pressure=float(request.POST['atmospheric_pressure'])
        density=(352.987*atmospheric_pressure)/(atmospheric_temperature+273)
        max_power_available=(0.5*density*3.14*(111/2)**2*wind_speed**3)/1000
        print(max_power_available)
        # load model
        model = joblib.load(r"C:\Users\HP\Downloads\RF_model.joblib")
        # Make prediction
        input=np.array([wind_speed,atmospheric_temperature,
        atmospheric_pressure,wind_direction,max_power_available]).reshape(1,-1)
        input=scaler.transform(input)
        result = model.predict(input)
        PredResult.objects.create(wind_speed=wind_speed,wind_direction=wind_direction,atmospheric_temperature=atmospheric_temperature,atmospheric_pressure=atmospheric_pressure,
        prediction=result)
        if wind_speed>3 or wind_speed<27:
            return redirect("result/")
        else:
            messages.error(request,'Please enter wind speeds between cut in and cut out speed')
    return render(request,'My_app/predict.html')

def view_result(request):
    data = PredResult.objects.last()
    return render(request, "My_app/result.html", {"data":f"{float(data.prediction):.2f}"})