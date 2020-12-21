from django.shortcuts import render


def index(request):
    return render(request, 'myapp/index.html')


def tourists_all(request):
    return render(request, 'myapp/tourists_all.html')

