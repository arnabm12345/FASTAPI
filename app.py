# 1. Library imports
import uvicorn
from fastapi import FastAPI
from NFLs import NFL
import numpy as np
import pickle
import pandas as pd
from fastapi.responses import JSONResponse

# 2. Create the app object
app = FastAPI()
# Load the trained model and scaler object from the same pickle file

pickle_in = open("lin_reg_model (1).pkl","rb")
lin_reg_model=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict')
def predict_NFL(data:NFL):
    Age = data.Age
    G = data.G
    GS = data.GS
    Cmp = data.Cmp
    Att = data.Att
    CmpPercent = data.CmpPercent
    Yds = data.Yds
    TD = data.TD
    TDPercent = data.TDPercent
    Int = data.Int
    IntPercent = data.IntPercent
    FirstDown = data.FirstDown
    Lng = data.Lng
    YPerA = data.YPerA
    AYPerA = data.AYPerA
    YPerC = data.YPerC
    YPerG = data.YPerG
    Sk = data.Sk
    YdsPerSk = data.YdsPerSk
    SkPercent = data.SkPercent
    NYPerA = data.NYPerA
    ANYPerA = data.ANYPerA
#    # print(lin_reg_model.predict([[variance,skewness,curtosis,entropy]]))
    scaled_features = [[Age, G, GS, Cmp, Att, CmpPercent, Yds, TD, TDPercent, Int, IntPercent, FirstDown, Lng, YPerA, AYPerA, YPerC, YPerG, Sk, YdsPerSk, SkPercent, NYPerA, ANYPerA]]
    # Make prediction
    prediction = lin_reg_model.predict(scaled_features)
    prediction_json = {'prediction': prediction.tolist()}  # Convert NumPy array to list
    return JSONResponse(content=prediction_json)


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload