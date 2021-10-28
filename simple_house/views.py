from django.shortcuts import redirect, render
from .models import Dish
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    dishes = Dish.objects.all()
    return render(request, 'index.html',{'dishes' : dishes})

@login_required(login_url='/accounts/login')
def dish(request,pk):
    dish = Dish.objects.filter(id=pk)
    return render(request,'dish.html',{'dish' : dish})
    