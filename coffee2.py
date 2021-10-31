import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    cm=[]
    sh=[]
    with open(data_path)as f:
        df=csv.DictReader(f)
        for row in df:
            cm.append(float(row["Coffee in ml"]))
            sh.append(float(row["sleep in hours"]))
    
    return {"x":cm,"y":sh}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource['y'])
    print("correlation is-",correlation[0,1])

def setup():
    data_path="coffee.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)

setup()