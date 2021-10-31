import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    icecreamsales=[]
    tp=[]
    with open(data_path)as f:
        df=csv.DictReader(f)
        for row in df:
            tp.append(float(row["Temperature"]))
            icecreamsales.append(float(row["Ice-cream Sales"]))
    
    return {"x":tp,"y":icecreamsales}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource['y'])
    print("correlation is-",correlation[0,1])

def setup():
    data_path="sales.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)

setup()