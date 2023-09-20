from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    contex = {
        
    }
    return HttpResponse(template.render(contex,request))

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')