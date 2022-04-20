import requests
import urllib.request, json
# Configure API request
def Place(zipcode):
    zipcode = int(zipcode)
    all_places = []
    endpoint = 'https://developer.nps.gov/api/v1/parks?limit=500&api_key=pKg0MiJOHZ2MxYHOhADpeIaLj8Yjh0r9wIbUL0Wj'
    #req = urllib.request.Request(endpoint)
    json_data = requests.get(endpoint).json() 
    #zipcode = int(input("get the input of your zip"))
    for park in json_data['data']:
        # print(park['fullName'])
        # print(park['addresses'][0]['postalCode'])
        if park['addresses'][0]['postalCode'] !='' and abs(zipcode-int(park['addresses'][0]['postalCode'][0:5])) <= 1000:
            all_places.append(park['fullName'])
            #print(park['fullName'])
    return all_places

















# #api_address = 'https://www.boredapi.com/api/activity'
# #api_address = 'https://api.nationalize.io?name='
# #api_address = 'https://v2.jokeapi.dev/joke/Any?type=single'
# api_address = 'https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=oE5mh2klCqhVjCiz7fGBGPCddnDw0y6JX2eXSmjB/visitorcenters'
# #name = input('give  name: ')
# #url = api_address + name 
# json_data = requests.get(api_address).json() 
# #format_add = json_data['address'] 
# print(json_data)             