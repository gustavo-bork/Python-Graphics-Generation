from plotly import graph_objects as go
# import requests
# import os
# from dotenv import load_dotenv
# import json

# load_dotenv()
# base_currency = 'CHF'
# url = f"https://api.apilayer.com/fixer/2022-04-16?symbols?USD&base={base_currency}"
# headers = { "apikey": os.getenv("API_KEY") }
# resp = requests.get(url, headers)
# print(json.loads(resp.text)['rates']['USD'])

"""
CHF - Franco suíço
GBP - Libra esterlina
EUR - Euro
USD - Dólar
Dados retirados da varíavel 'url'. Para verificar, descomentar o código acima e substituir a variável base_currency
por um dos valores abaixo
"""
CHF = 1.060323
GBP = 1.036
EUR = 1.08438

locations = ['Spain', 'Portugal', 'France', 'Belgium', 'Netherlands', 'Germany', 'Austria', 'Ireland', 'Italy', 'Greece', 'Slovakia', 'Slovenia', 'Cyprus', 'Estonia', 'Latvia', 'Lithuania', 'Finland', 'Switzerland', 'Great Britain']

data = dict(
    type='choropleth', 
    locationmode='country names', 
    colorscale=['blue', 'yellow'],
    locations=locations, 
    z=[EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, EUR, CHF, GBP]
)

map = go.Figure(data=[data])
map.update_layout(title_text='Valor do euro, do franco suíço e da libra esterlina no dia 16/04/2022 (em dólares)')
map.update_geos(scope='europe')
map.show()