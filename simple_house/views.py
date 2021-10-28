from django.shortcuts import render
from .models import Dish

# Create your views here.
def index(request):
    dishes = Dish.objects.all()
    return render(request, 'index.html',{'dishes' : dishes})


