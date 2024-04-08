import requests

url = "http://localhost:8000/guess"
jsonPlayer = {
    "player":"Julian"
}
#creando partida
requ = requests.post(url,json=jsonPlayer)
print(requ.text)
#mostrand
requ = requests.get(url)
print(requ.text)
#params
requ = requests.get(url+"/",params="player=Julian")
print(requ.text)
# #put
requ = requests.put(url+"/1",json={"attempt":"25"})
print(requ.text)
#mostrand
requ = requests.get(url)
print(requ.text)
# #put
requ = requests.put(url+"/1",json={"attempt":"75"})
print(requ.text)
#mostrand
requ = requests.get(url)
print(requ.text)
# #put
requ = requests.put(url+"/1",json={"attempt":"50"})
print(requ.text)
#mostrand
requ = requests.get(url)
print(requ.text)
#delete
requ = requests.delete(url+"/1")
print(requ.text)
requ = requests.get(url)
print(requ.text)
