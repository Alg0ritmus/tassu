# Python Scripty
Získavanie a spracovaie údajov je jedným zo základných krokov, ktoré je potrebné podstúpiť pri riešeni tohto projektu. Pri získavaní dát o meste Snina sme použili viaceré techniky získavania dát ako napríklad WebScraping alebo privátnu API. Pri týchto technikách sme využili programovací jazyk Python verzie 3.10.4.


## Digitálne mesto

Prvým zdrojom dát, ktorý sme využili v rámci tohto projektu, je stránka www.digitalnemesto.sk.
Na tejto linke môžeme vidieť rôzne informácie ohľadom krajských miest, ktoré sú vhodné pre analýzu dát tohto projektu. Tento zdroj dát považujeme za dôveryhodný a kvantitatívne postačujúci pre vytvorenie základnej "kostry" nášho projektu. Konkrétne pre nami zvolené  mesto Snina tu nájdeme vaic ako 24-tisíc záznamov rôzných dát (faktúry v rámci vejerjného obstarávania mesta Snina).

---

Script, ktorý je využitý v tomto prípade (súbor main.py & skuska_json.py) je založený na princípe reverzného inžinierstva, kde z privátnej API (ktorú použiva daný zdroj) vieme vhodnou analýzov a úpravou požiadávky (request) na server získať chcené údaje vo forme 'application/json' odpovede (response). Tento script je možné detailne analyzovať v súbore main.py. Dôležitým krokom je vhodne nastaviť TLS adaptér a to tak, aby bola zabezpečená kompatibilita SLL certifikátu so zdrojom (serverom). Viac je možné nájsť priamo v scripte (main.py).  

Následne sme JSON súbor konvertovali do formátu CSV, ktorý je vhodný pre nahrávanie dát do databázy MySQL. Konverziu zabezpečíme funkciami, ktoré sú dostupné v súbore skuska_json.py.
