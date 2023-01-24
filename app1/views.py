from django.shortcuts import render
from app1.models import Profession

def index_page(request):
    data = {
         'profession': Profession.objects.get(id=2)
    }
    return render(request, "index.html", context=data)

def skills_page(request):
    data = {
        'search_url': 'ddd'
    }
    return render(request, "skills.html", context=data)
