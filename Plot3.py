from urllib import request
from matplotlib.pyplot import colorbar
from plotly import graph_objects as go

# # Moedas comparadas:
# # CHF - Franco suíço
# # GBP - Libra esterlina
# # EUR - Euro
# # USD - Dólar
# # Dados retirados da varíavel 'url'. Para verificar, descomentar o código abaixo
# import requests
# base_currency = 'EUR'
# url = f"https://api.apilayer.com/fixer/2022-04-16?symbols?USD&base={base_currency}"
# headers = { "apikey": "7bsw5Cw47URoFCdDngHsGZRrcTVC0gC4" }
# resp = requests.get(url, headers)
# print(resp.text)

locations = [ 'Spain', 'Portugal', 'France', 'Belgium', 'Netherlands', 'Germany', 'Austria', 'Ireland', 'Italy', 'Greece', 'Slovakia', 'Slovenia', 'Cyprus', 'Estonia', 'Latvia', 'Lithuania', 'Finland', 'Switzerland', 'Great Britain' ]

data = dict(
    type='choropleth', 
    locationmode='country names', 
    colorscale=['blue', 'yellow'],
    locations=locations, 
    z=[ 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.081438, 1.060323, 1.036 ]
)

map = go.Figure(data=[data])
map.update_layout(title_text='Valor do euro, do franco suíço e da libra esterlina no dia 16/04/2022 (em dólares)')
map.update_geos(scope='europe')
map.show()