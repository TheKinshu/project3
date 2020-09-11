from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def menu(request):
    return render(request, "orders/menu.html")
    
def direction(request):
    return render(request, "orders/direction.html")

def hours(request):
    return render(request, "orders/hours.html")

def svr(request):
    return render(request, "orders/svr.html")

def contact(request):
    return render(request, "orders/contact.html")

def cart(request):
    return render(request, "orders/cart.html")
