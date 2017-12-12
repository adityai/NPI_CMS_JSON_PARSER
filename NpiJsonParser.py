import json
import requests

def main():
	url = "https://npiregistry.cms.hhs.gov/api?number=1285005603"
	r = requests.get(url)
	print (r.status_code)
	jsonString = json.loads(r.text)
	first_name = jsonString['results'][0]['basic']['first_name']
	last_name = jsonString['results'][0]['basic']['last_name']
	print (first_name)
	print (last_name)

main()
