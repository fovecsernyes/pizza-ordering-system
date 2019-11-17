from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('pizzak/', views.pizzas, name='pizzas'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('pizzalist/', views.pizzalist, name='pizzalist'),
    path('myorders/', views.myorders, name='myorders'),
    path('pizzalist/pizzaSearch', views.pizzasearch, name='pizzasearch'),
]
