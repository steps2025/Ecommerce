from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("products/<int:category_id>/", views.products, name="products"),
    path("specific_subcategory/<int:subproduct_id>/",views.specific_subcategory,name="specific_subcategory"),
    path("single_product/<int:product_id>/", views.single_product, name="single_product"),
]