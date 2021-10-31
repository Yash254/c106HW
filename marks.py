import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    mp=[]
    dp=[]
    with open(data_path)as f:
        df=csv.DictReader(f)
        for row in df:
            mp.append(float(row["Marks In Percentage"]))
            dp.append(float(row["Days Present"]))
    
    return {"x":mp,"y":dp}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource['y'])
    print("correlation is-",correlation[0,1])

def setup():
    data_path="marks.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)

setup()