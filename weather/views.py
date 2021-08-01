from django.shortcuts import render

import urllib.request
import json

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        c2 = city.replace(" ", "+")
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + c2 + '&units=metric&appid=1d01f8fe40dcf2b004c5d7708dd5080f').read()
        # source2 = urllib.request.urlopen('http://pro.openweathermap.org/data/2.5/forecast/hourly?q=' + c2 + '&units=metric&appid=1d01f8fe40dcf2b004c5d7708dd5080f').read()
        list_of_data = json.loads(source)
        # list_of_data2 = json.loads(source2)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "windspeed": str(list_of_data['wind']['speed']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],

            # "temph": str(list_of_data2['main']['temp']) + ' °C',
            # "mainh": str(list_of_data2['current']['weather'][0]['main']),
            # "descriptionh": str(list_of_data2['current']['weather'][0]['description']),
            # "iconh": list_of_data2['current']['weather'][0]['icon'],


            # "tempd": str(list_of_data['daily']['temp']['min']) + ' °C' + str(list_of_data['daily']['temp']['max']) + ' °C',
            # "maind": str(list_of_data['daily']['weather'][0]['main']),
            # "descriptiond": str(list_of_data['daily']['weather'][0]['description']),
            # "icond": list_of_data['daily']['weather'][0]['icon'],
        }
        # print(data)
    else:
        data = {}    
    
    
    return render(request,'main/home.html', data)
