from django.urls import path

from . import views

urlpatterns =  [
    path("", views.index, name="index"),
    path("<int:voo_id>", views.voo, name="voo"),
    path("<int:voo_id>/comprar", views.comprar, name="comprar"),
]