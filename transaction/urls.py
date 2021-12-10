from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListTrans.as_view,name="list_trans"),
    

]