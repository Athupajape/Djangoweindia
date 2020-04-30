from django.shortcuts import render

def home(request):
    import json
    import requests
    import datetime

    if request.method == "POST":
        state = request.POST['state']
        api_request=requests.get("http://api.openweathermap.org/data/2.5/weather?APPID=4d6a9cf1af465c6f76e25f5166077493&q="+state)
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="Error..."
        
        return render(request,'home.html',{'api':api})         
    else:    
        api_request=requests.get("http://api.openweathermap.org/data/2.5/weather?APPID=4d6a9cf1af465c6f76e25f5166077493&q=solapur")
            
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="Error..."  
        if api['weather'][0]['main'] == "clouds":
            weather_info="clouds"
        elif api['weather'][0]['main'] == "haze":
            weather_info="haze"
        elif api['weather'][0]['main'] == "rain":
            weather_info="rain"
        elif api['weather'][0]['main'] == "thunderstorm":
            weather_info="thunderstorm"        
        return render(request,'home.html',{'api':api})    
    



# http://api.openweathermap.org/data/2.5/weather?APPID=4d6a9cf1af465c6f76e25f5166077493&q=Mumbai