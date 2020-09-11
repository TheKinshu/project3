from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("direction", views.direction, name="direction"),
    path("hours", views.hours, name="hours"),
    path("svr", views.svr, name="svr"),
    path("contact", views.contact, name="contact"),
    path("cart", views.cart, name="cart"),
]
