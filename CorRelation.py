import csv
from os import X_OK
import numpy as np
import ploty.express as px
def getDataSource(data_path):
    ice_cream_sales = []
    cold_drinks_sales = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Ice Cream Sales"]))
    return{x:ice_cream_sales, y:cold_drinks_sales}

def findCorRelation(data_source)
    correlation = np.np.corrcoef(data_source["x"], data_source["y"])
    print("CorRelation Between Temperature And Ice Cream", correlation[0, 1])
def setup():
    data_path = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data_source = getDataSource(data_path)
    findCorRelation(data_source)
setup()