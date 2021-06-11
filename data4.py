import csv
import plotly.express as px
with open("Student Marks vs Days Present.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Student Marks", y = "Days Present")
    fig.show()