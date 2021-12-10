from products.models import categories, products
from django.http.response import Http404
from django.shortcuts import render , redirect
from random import choice
# # Create your views here.
def account(req):
    if req.user.is_authenticated:
        username = req.user.username
        first_name = req.user.first_name
        last_name = req.user.last_name
        return redirect("dashboard")
    if req.method == "GET":
        return render(req,"account/account.html")

def dashboard(req):
        superuser = False
        if req.user.is_superuser:
            superuser = True
        if req.user.is_authenticated:
            log = True
        else:
            log = False
        p = products.objects.filter(deleted=False)
        ps = []
        for i in p:
            ps.append(i)
        suggests = []
        for i in range(5):
            product = choice(ps)
            suggests.append([product.name,product.category.parent.name,product.price,product.id,product.picture.url])
            ps.remove(product)
        print(req.user.username)
        return render(req,"account/dashboard.html",{"suggests":suggests,"log":log,"super":superuser})

def login(req):
    if req.method == 'POST':
        from django.contrib.auth import authenticate, login
        username = req.POST.get('username',None)
        password = req.POST.get('password',None)
        user = authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect("dashboard")
        else:
            return render(req, "account/Login.html", {"error": "ورود نامعتبر"})

    elif req.method == 'GET':
        return render(req,'account/Login.html')
    else:
        return Http404()

def register(req):
    if req.method == 'POST':
        from django.contrib.auth.models import User
        
        full_name = req.POST.get('fullname',None)
        if isinstance(full_name,str) and full_name.index(" ") > 0:
            first_name , last_name = full_name.split()
        
        username = req.POST.get('username',None)
        password = req.POST.get('password',None)
        confirm_pass = req.POST.get('confirm_password',None)
        email = req.POST.get('email',None)
        if password != confirm_pass:
            return render(req, "account/register.html", {"error": "رمز خود را دوباره وارد کنید"})
        
        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('login')
        
    elif req.method == 'GET':
        if req.user.is_authenticated:
            return redirect("dashboard")
        else:
            return render(req,'account/register.html')
    else:
        return Http404()

def _logout(req):
    if req.user.is_authenticated:
        from django.contrib.auth import logout
        logout(req)
    
    return redirect("login")


def ex(req):
    return render(req,"product/e-commerce.html")