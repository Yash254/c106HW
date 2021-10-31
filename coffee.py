import plotly.express as px
import csv

with open("coffee.csv")as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="sleep in hours",y="Coffee in ml")
    fig.show()