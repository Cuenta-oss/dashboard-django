from django.urls import path
from . import views

urlpatterns = [
    path("about/",  views.about, name='about'),
    path("contact/", views.contact, name="contact"),
    path("add_products/", views.addProduct, name="add_products"),
    path("list_productos/", views.listProduct, name="list_productos"),
    path("edit_product/<int:id>/", views.editProduct, name="edit_product"),
    path("del_product/<int:id>/", views.del_product, name="del_product"),
]