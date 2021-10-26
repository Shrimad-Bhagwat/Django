from django.shortcuts import render
from .models import Dish

# Create your views here.
def index(request):

    dish1 = Dish()
    dish1.name = "Salad"
    dish1.desc = "A mixture of raw usually green leafy vegetables (as lettuce) combined with other vegetables (as tomato and cucumber) and served with a dressing."
    dish1.price = 10
    dish1.img = '01.jpg'
    dish1.discount = False

    dish2 = Dish()
    dish2.name = "Pizza"
    dish2.desc = "A dish made typically of flattened bread dough spread with a savory mixture usually including tomatoes and cheese and often other toppings and baked"
    dish2.price = 25
    dish2.img = '02.jpg'
    dish2.discount = True

    dish3 = Dish()
    dish3.name = "Garlic Bread"
    dish3.desc = "It consists of bread topped with garlic and olive oil or butter and may include additional herbs, such as oregano"
    dish3.price = 20
    dish3.img = '03.jpg'
    dish3.discount = False

    dish4 = Dish()
    dish4.name = "Pasta"
    dish4.desc = "Pasta is a type of food typically made from an unleavened dough of wheat flour mixed with water or eggs, and formed into sheets or other shapes"
    dish4.price = 36
    dish4.img = '04.jpg'
    dish4.discount = True

    dishes = [dish1, dish2, dish3, dish4]
    return render(request, 'index.html',{'dishes' : dishes})


