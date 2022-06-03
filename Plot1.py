from tkinter.ttk import LabeledScale
from urllib import request
from matplotlib import pyplot
from dotenv import load_dotenv
import numpy as np
import os
import requests
import json
from datetime import date, timedelta

# Função usada uma única vez, caso não tenha o arquivo values.json
def getAPIValues():
    load_dotenv()
    headers = { "apikey": os.getenv("API_KEY") }
    first_date = date(2021, 5, 29)
    last_date = date(2022, 5, 29)

    url = f"https://api.apilayer.com/fixer/timeseries?base=EUR&symbols=USD&start_date={first_date.isoformat()}&end_date={last_date.isoformat()}"
    response = requests.get(url, headers)

    file = open("values.json", "w")
    file.write(response.text)
    
    print("Valores passados com sucesso")

def generatePlotGraphics():
    values = [] 
    dates = []
    with open('values.json') as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

        for i in range(365):
            data = date(2021, 5, 29) + timedelta(days=i)
            dates.append(data.strftime("%x"))
            values.append(jsonObject['rates'][data.isoformat()]['USD'])
    
    pyplot.plot(values, color='r')

    pyplot.ylabel("Valor (em dólares)")
    pyplot.yticks(ticks=[1.05, 1.10, 1.15, 1.2, 1.25], labels=["1,05", "1,10", "1,15", "1,20", "1,25"])

    pyplot.xlabel("Data (Entre 2021 e 2022)")
    xlabels=["29/05", "29/06", "29/07", "29/08", "29/09", "29/10", "29/11", "29/12", "29/01", "28/02", "29/03", "29/04", "29/05"]
    pyplot.xticks(ticks=[0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360], labels=xlabels)
    
    pyplot.title("Valor do Euro (em dólares)")
    pyplot.show()

getAPIValues()
generatePlotGraphics()