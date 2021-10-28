from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dish/<int:pk>',views.dish,name='dish'),
]
