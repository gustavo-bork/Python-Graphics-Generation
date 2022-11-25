from dotenv import load_dotenv
import os
import requests
from datetime import date

try:
  load_dotenv()
  
  first_date = date(2021, 5, 29)
  last_date = date(2022, 5, 29)

  headers = { "apikey": os.getenv("API_KEY") }
  url = f"https://api.apilayer.com/fixer/timeseries?base=EUR&symbols=USD&start_date={first_date.isoformat()}&end_date={last_date.isoformat()}"
  response = requests.get(url, headers)

  file = open("values.json", "w")
  file.write(response.text)

  print("Valores passados com sucesso")
except:
  print("Não foi possível buscar os valores")
