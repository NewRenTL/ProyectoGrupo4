import requests
from flask import jsonify
import json

import requests
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

querystring = {"ingredients":"apples,flour,sugar","number":"5","ignorePantry":"true","ranking":"1"}

headers = {
	"X-RapidAPI-Key": "f339e98814msh8d19be96b42f447p1eb434jsnfd981f16175d",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers,params=querystring)

#response_str = response.text
response_json = response.json()

print(len(response_json))
for i in range(0,len(response_json)):
	print(response_json[i]['title'])
with open('api.json','w') as file:
    json.dump(response_json, file,indent=4)
#print(response_json)