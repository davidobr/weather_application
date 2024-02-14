import requests
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from api_key import API as api_key
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "weather_application/home.html", {'user': request.user})


@login_required
def weather(request):
    if request.method == "POST":
        city = request.POST.get('city')  # Replace 'city' with the name of your form input field
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        weather_data = response.json()
        return render(request, 'weather_application/weather.html', {'weather_data': weather_data})
    else:
        return render(request, 'weather_application/weather.html')


def logout_view(request):
    logout(request)
    return redirect('home')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
