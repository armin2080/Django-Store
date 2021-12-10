from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="factor"),
    path("factors",views.listfactors,name="listFactors"),
    path("delete/<int:id_factor>",views.deleteFactor,name="delete_factor"),
    path("purchase/<int:id_fac>",views.purchase,name="purchase"),
    path('get_factor/<int:id_fac>',views.getFactor,name="get_factor"),

]