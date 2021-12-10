from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class ListTrans(View):
    template_file = ''

    def get(self,request,*args,**kwargs):
        return HttpResponse("List Trans {get} ")

    def post(self,request,*args,**kwargs):
        return HttpResponse("List Trans {post}")