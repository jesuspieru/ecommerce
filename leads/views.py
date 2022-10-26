from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    context = {
        "name": "Joe",
        "age": 35,
    }
    return render(request, "leads/home.html", context)