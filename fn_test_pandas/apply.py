import numpy as np
import pandas as pd
import os
import json


boolean=[True,False]
gender=["男","女"]
color=["white","black","yellow"]
data=pd.DataFrame({
    "height":np.random.randint(150,190,100),
    "weight":np.random.randint(40,90,100),
    "smoker":[boolean[x] for x in np.random.randint(0,2,100)],
    "gender":[gender[x] for x in np.random.randint(0,2,100)],
    "age":np.random.randint(15,90,100),
    "color":[color[x] for x in np.random.randint(0,len(color),100) ]
}
)

def BMI(series):
    weight = series["weight"]
    height = series["height"]/100
    BMI = weight/height**2
    return json.dumps(BMI)
data["BMI"] = data.apply(BMI, axis=1)
print(data)