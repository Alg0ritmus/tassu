import requests
import ssl
from urllib3 import poolmanager

url = "https://snina.digitalnemesto.sk/DmApi/fakturyDodavatelske?_dc=1667327215227&organizaciaId=157&year=2022&page=1&start=0&limit=25"

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

print(res)
client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
print(client_context.security_level)