import csv
import plotly.express as px
with open("Size of TV,_Average time spent watching TV.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Size of TV", y = 'Average time spent watching TV')
    fig.show()