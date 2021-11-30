import geopy.distance
import json
from MiniScripts.api_key import API_KEY
import requests

def calc_distance(lat1,lng1,lat2,lng2):
    coords_1 = (lat1, lng1)
    coords_2 = (lat2, lng2)
    return geopy.distance.distance(coords_1, coords_2).km

def calc_driving_distance(lat1,lng1,lat2,lng2):
    url = f'''https://maps.googleapis.com/maps/api/distancematrix/json?origins={lat1}%2C{lng1}&destinations={lat2}%2C{lng2}&key={API_KEY}'''

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    responseData=json.loads(response.text)
    if(responseData['status']=='OK'):
        distance=responseData["rows"][0]["elements"][0]["distance"]["value"]/1000
        return distance
    else:
        return 0.0

def calc_pixels(x,y):
    xpos = (-18.67870 * pow(x,4)) + 2344.64935* pow(x,3)-110330.13041*pow(x,2)+2306889.77548*x-18085207.56888
    ypos= -122.23919*pow(y,4)+14992.73104*pow(y,3)-689533.76977*pow(y,2)+14093270.30405*y-108007280.96092
    return (xpos,ypos)
