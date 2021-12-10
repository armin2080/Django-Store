from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='cart'),
    path('add/<int:product_id>',views.add,name="add_to_cart"),
    path('delete/<int:id_cart>',views.delete,name="delete_cart"),
    path('addCart/<int:id_cart>',views.addCart,name="addCart"),
    path('remove/<int:id_cart>',views.remove,name='remove')
    # path('preFactor',views.pre_factor,name="pre_factor")
]