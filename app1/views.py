from django.shortcuts import render
from app1.models import Profession

def index_page(request):
    data = {
         'profession': Profession.objects.get(id=2)
    }
    return render(request, "index.html", context=data)

def skills_page(request):
    data = {
        'images': 'ddd'
    }
    return render(request, "skills.html", context=data)

def vacs(request):
    data = {

    }
    return render(request, "vacs.html", context=data)

def geo(request):
    data = {

    }
    return render(request, "geo.html", context=data)

def topicaluty(request):
    data = {

    }
    return render(request, "topicality.html", context=data)