# P.Z. Tassu ci jak
# inspired by: https://datatofish.com/json-string-to-csv-python/
# https://stackoverflow.com/questions/61631955/python-requests-ssl-error-during-requests


import pandas as pd

import http.client
import json
import requests

import requests
import ssl
from urllib3 import poolmanager
import skuska_json_to as converter


# url, payload, headers ziskaj z Postmana

url = "https://snina.digitalnemesto.sk/DmApi/fakturyDodavatelske?_dc=1666199922124&organizaciaId=157&year=0&page=1&start=0&limit=25"

payload={}
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'sk',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json;',
  'Referer': 'https://snina.digitalnemesto.sk/zverejnovanie/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}



# edit TLS adapter (ak tento krok preskocime, dostaneme error)
# vysvetlenie: digitalnemesto.sk pouziva zastaraly protokol,
# preto je potrebne prisposobit TLS adapter pre danu stranku
# viac na:
# # https://stackoverflow.com/questions/61631955/python-requests-ssl-error-during-requests
class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        #Create and initialize the urllib3 PoolManager.
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)

session = requests.session()
session.mount('https://', TLSAdapter())
res = session.request("GET", url, headers=headers, data=payload)


# converter.JSON_to_CSVfile(Json_obj,"my_filename")

# output >> my_filename.csv
converter.JSON_to_CSVfile(json.loads(res.text),"skuska2")



# CSV file to Excel
converter.CSVfile_to_Excelfile("skuska2")