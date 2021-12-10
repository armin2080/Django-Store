from django.shortcuts import redirect, render
from .models import Factors,FactorProducts
from cart.models import Cart
from products.models import products
# Create your views here.

def index(req):
    if req.user.is_authenticated:
        carts = Cart.objects.filter(id_user= req.user)
        if len(carts) == 0:
            return(redirect('cart'))

        f = None
        if f == None:
            price = 0
            for c in carts:
                price += int(c.total_price)
            fac = Factors()
            fac.id_user=req.user
            fac.state = 1
            fac.total_price = price
            fac.save()
            for c in carts:
                f_p = FactorProducts()
                f_p.id_factor = fac
                f_p.id_products = c.id_product
                f_p.count = c.count
                f_p.total_price = c.total_price
                f_p.save()
            list_of_fp = []
            fp = FactorProducts.objects.filter(id_factor=fac)
            for i in fp:
                list_of_fp.append([i.id_products.name,i.count,i.total_price,i.id_products.id , i.id_products.price])
            factor = [fac.id_user.username,fac.payment_date,fac.state,fac.create_date,fac.total_price,fac.id]
            for c in carts:
            
                carts.delete()
            
            return render(req,"factor/index.html",{"fp":list_of_fp,"f":factor})
    else:
        return redirect('dashboard')
    # else:
    #     c = Cart.objects.filter(id_user=req.user)
    #     Cart_list = []
    #     for i in c:
    #         Cart_list.append([i.id_product.name,i.id_user.username,i.count,i.total_price,i.id])
    
    #     return render(req,'cart/index.html',{"products":Cart_list,"error1":"ابتدا فاکتور پرداخت نشده را پرداخت کنید"})
        
            
def listfactors(req):
    if req.user.is_authenticated:
        factors = Factors.objects.filter(id_user=req.user)
        f_list = []
        for f in factors:
            f_list.append([f.id_user.username,f.payment_date,f.state,f.create_date,f.total_price,f.id])
        return render(req,"factor/factors.html",{"factors":f_list})
    else:
        return redirect('login')

def deleteFactor(req,id_factor):
    f = Factors.objects.get(id=id_factor)
    fp = FactorProducts.objects.filter(id_factor=f)

    for p in fp:
        
        product = products.objects.get(id=p.id_products.id)
        product.count += int(p.count)
        product.save()
    f.delete()
    return redirect("listFactors")

def purchase(req,id_fac):
    fac = Factors.objects.get(id=id_fac)
    fac.state = 3
    fac.save()
    return redirect('listFactors')

def getFactor(req,id_fac):
    f = Factors.objects.get(id=id_fac)
    fp = FactorProducts.objects.filter(id_factor=f)
    list_of_fp = []
    for i in fp:
        list_of_fp.append([i.id_products.name,i.count,i.total_price,i.id_products.id,i.id_products.price])
    factor = [f.id_user.username,f.payment_date,f.state,f.create_date,f.total_price,f.id]
    return render(req,"factor/index.html",{"fp":list_of_fp,"f":factor})