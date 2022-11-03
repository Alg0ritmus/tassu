# https://www.orsr.sk/hladaj_ico.asp?ICO=36490750
import requests
from bs4 import BeautifulSoup
import json
ROLA = {"Štatutárny orgán":"Konateľ","Spoločníci":"Spoločník"}


def without_redundancy(arr):

	
	_dict = {}

	for item in arr:
		if len(item)>0:
			if str(item[0])+str(item[1]) not in _dict:
				_dict[str(item[0])+str(item[1])] = item
		

	
	return [_dict[i] for i in _dict]

#url = 'https://www.orsr.sk/hladaj_ico.asp?ICO=36463825'
#url = 'https://www.orsr.sk/hladaj_ico.asp?ICO=36490750'
def get_url_by_ICO(url):
	
	req = requests.get(url,allow_redirects=False)
	raw_content = req.content.decode(encoding="ISO-8859-1")
	soup = BeautifulSoup(raw_content,'html.parser')


	hrefs = soup.find_all("a", {"class": "link"})

	my_url=[]
	for href in hrefs:
		if "vypis" in str(href):
			my_url.append(href.get("href"))
			#print("VYPIS\n"+str(href)+"\n")
	return my_url[-1]









def get_konatelia_spolocnici(url,rola):

	origin_plus_url = "https://www.orsr.sk/"+str(url)
	fullname = []
	konatelia = []


	req = requests.get(origin_plus_url,allow_redirects=False)
	req.encoding = req.apparent_encoding
	soup = BeautifulSoup(req.text,'html.parser')

	#print(soup.prettify())
	hrefs = soup.find_all("span", {"class": "tl"})
	for href in hrefs:
		if str(rola) in str(href):
			tmp = href.parent.find_next_siblings("td")
			for i in tmp:
				array_of_spol = i.find_all("table")

	
	
	#print(array_of_spol)

	
	slovo = ""
	for table in array_of_spol:
		all_info = []
		#print(span.text)
		for tr in table:
			if tr.find("a") != -1 and tr.find("a") != None :
				_meno =tr.find("a")

				for i in _meno.next_siblings:
					slovo += i.text
					if "<br" in str(i):
						all_info.append(slovo.strip())
						slovo = ""
				all_info.append(ROLA[rola])
				#print("siblings:",_meno.span.next_sibling)
				_meno_arr = _meno.text.split("   ")
				all_info.insert(0,_meno_arr[1])
				all_info[1] = _meno_arr[2]

		konatelia.append(all_info)



	konatelia = without_redundancy(konatelia)

	return konatelia
	



def get_summary(url):
	spolocnici_podla_ica=get_url_by_ICO(url)
	statutari = get_konatelia_spolocnici(spolocnici_podla_ica,"Štatutárny orgán")
	spolocnici = get_konatelia_spolocnici(spolocnici_podla_ica,"Spoločníci")

	arr = statutari+spolocnici

	_dict = {}

	for item in arr:
		if len(item)>0:
			if str(item[0])+str(item[1]) not in _dict:
				_dict[str(item[0])+str(item[1])] = item
			else:
				item[-1] = ROLA["Štatutárny orgán"]+"/"+ROLA["Spoločníci"]
				_dict[str(item[0])+str(item[1])] = item

	return [_dict[i] for i in _dict]


#print(get_summary(url))





def scrapeAll(ICOs_file):
	f = open(ICOs_file,"r")
	raw_JSON_data = f.read()
	f.close()

	ICOs = json.loads(raw_JSON_data)["ICOs"]


	partial_url = 'https://www.orsr.sk/hladaj_ico.asp?ICO='
	for ico in ICOs:
		try:
			print(partial_url+str(ico))
			print(get_summary(partial_url+str(ico)))
		except Exception as e:
			print("Error",e)
			pass



scrapeAll("ICA_skuska.json")