import requests
from django.shortcuts import render
from api_key import API as api_key


def homepage(request):
    if request.method == "POST":
        city = request.POST.get('city')  # Replace 'city' with the name of your form input field
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        weather_data = response.json()
        return render(request, 'weather_application/homepage.html', {'weather_data': weather_data})
    else:
        return render(request, 'weather_application/homepage.html')
