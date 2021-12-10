from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from cart.models import Cart

from products.models import products

# Create your views here.

def index(req):
    if req.user.is_authenticated == True:
        c = Cart.objects.filter(id_user=req.user)
        Cart_list = []
        for i in c:
            Cart_list.append([i.id_product.name,i.id_user.username,i.count,i.total_price,i.id,i.id_product.picture.url])
    
        return render(req,'cart/index.html',{"products":Cart_list})
    else:
        return redirect('dashboard')


def add(req,product_id):
    if req.user.is_authenticated:
        try:
            carts = Cart.objects.get(id_product=product_id,id_user = req.user)
        except:
            carts = None
        p = products.objects.get(id=product_id)
        if carts == None:
            if p.count > 0:
                c = Cart()
                c.id_product = p
                c.id_user = req.user
                c.count = 1
                c.total_price = int(p.price)
                c.save()
                p.count -= 1
                p.save()
            return HttpResponseRedirect(reverse("get_product",kwargs={"id_product":product_id}))
            

        else:
            if p.count > 0:

            
                carts.count += 1
                carts.total_price += int(p.price)
                carts.save()
                p.count -= 1
                p.save()
            return HttpResponseRedirect(reverse("get_product",kwargs={"id_product":product_id}))
    else:
        return redirect("account")    

def addCart(req,id_cart):
    c = Cart.objects.get(id=id_cart)
    p = c.id_product
    if p.count > 0:
        c.count += 1
        c.total_price += int(p.price)
        p.count -= 1
        c.save()
        p.save()
        return redirect('cart')
    else:
        return redirect('product')

def delete(req,id_cart):
    c = Cart.objects.get(id=id_cart)
    p = c.id_product
    c.count -= 1
    c.total_price -= int(p.price)
    p.count += 1
    
    c.save()
    p.save()
    if c.count == 0:
        c.delete()
    return redirect('cart')

def remove(req,id_cart):
    c = Cart.objects.get(id=id_cart)
    p = c.id_product
    p.count += c.count
    c.delete()
    p.save()
    
    return redirect('cart')