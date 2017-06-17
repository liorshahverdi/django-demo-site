from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    return render(request, 'investigator/index.html', {})

def search(request):
    return HttpResponse("You have made it to the search index.")
