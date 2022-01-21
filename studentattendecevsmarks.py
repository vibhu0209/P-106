# relation between number of days each student has been present in college in a year
# vs 
# the percentage of marks scored in the half-yearly exams
import numpy as np
import csv 
import plotly.express as px

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    Marks = []
    attendance = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            attendance.append(float(row["Days Present"]))
            Marks.append(float(row["Marks In Percentage"]))
    return{"x": attendance, "y": Marks}
    
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between attendance and Marks is ", correlation[0,1])

def setup():
    data_path = "E:\WHITEHAT JR\python\P-106\Marks.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)
    
setup()
