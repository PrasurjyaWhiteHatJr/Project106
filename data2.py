import csv
import plotly.express as px
with open("cups of coffee vs hours of sleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Coffee", y = "sleep")
    fig.show()