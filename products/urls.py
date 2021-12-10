from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name="product"),
    path('add', views.add, name="add_product"),
    path('delete/<int:id_cat>', views.delete, name="delete_product"),
    path('edit/<int:id_cat>', views.edit, name="edit_product"),
    path('get/subcategories', views.get_subcategories, name="get_subcategories"),
    path('get/product/<int:id_product>',views.get_product,name="get_product"),
    path('categories',views.category,name="categories"),
    path('subcategories/products/<int:id_sub>',views.subProducts,name="sub_products")
]