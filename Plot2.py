from datetime import date, timedelta
import json
from matplotlib import pyplot
import numpy as np

values = [] 
dates = []
with open('values.json') as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

    for i in range(365):
        data = date(2021, 5, 29) + timedelta(days=i)
        dates.append(data.strftime("%x"))
        values.append(jsonObject['rates'][data.isoformat()]['USD'])

bar1 = list(filter(lambda x: (x >= 1.2), values))
bar2 = list(filter(lambda x: (x >= 1.15 and x < 1.2), values))
bar3 = list(filter(lambda x: (x >= 1.1 and x < 1.15), values))
bar4 = list(filter(lambda x: (x >= 1.05 and x < 1.1), values))

indices = np.arange(4)

pyplot.bar(indices, [len(bar1), len(bar2), len(bar3), len(bar4)])
pyplot.xlabel('Valor do Euro (em US$)')
pyplot.xticks(indices, ['Mais de 1,20', 'Entre 1,15 e 1,20', 'Entre 1,10 e 1,15', 'Entre 1,05 e 1,10'])
pyplot.ylabel('Quantidade de dias')
pyplot.title('Número de dias em que o Euro ficou entre determinado intervalo de valores')
pyplot.show()