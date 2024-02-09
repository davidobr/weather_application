from django.shortcuts import render


def homepage(request):
    return render(request, 'weather_application/homepage.html')
