from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from products.models import categories, products, subcategories



def index(req):
    # todo: check login for specialist
    from .models import products,categories

    # select all categories
    cat = categories.objects.all()
    list_of_cat = []
    for i in cat:
        list_of_cat.append([i.id,i.name])
    
    

    # select all products
    p = products.objects.filter(deleted=False)
    list_of_product = []
    for i in p:
        list_of_product.append([i.name, i.count, i.price, i.category.name, i.id,i.picture.url])
    
    if req.user.is_superuser == True:
        return render(req, "product/index.html", {"list": list_of_product, "categories":list_of_cat})
    else:
        return redirect('dashboard')

def add(req):
    if req.method == "POST":
        name_product = req.POST.get("name_product", False)
        price_product = req.POST.get("price_product", False)
        count_product = req.POST.get("count_product", False)
        subcategory_product = req.POST.get("subcategory_product", False)
        if False in [name_product, price_product, count_product, subcategory_product]:
            return redirect("product")
        from .models import products, subcategories

    
        s_c = subcategories.objects.get(id=subcategory_product)
           
          
        p = products()
        p.name = name_product
        p.price = int(price_product)
        p.count = int(count_product)
        p.category = s_c
        p.save()
        
        return redirect("product")
    else:
        return Http404()
    


def delete(req, id_cat=None):
    if not id_cat:
        redirect("product")

    from .models import products

    p = products.objects.get(id=id_cat)
    # p.delete()
   
    p.deleted = True
    p.save()
  
    return redirect("product")
    


def edit(req, id_cat=None):

    from .models import products, subcategories
    
    if req.method == "POST":
        name_product = req.POST.get("name_product", False)
        price_product = req.POST.get("price_product", False)
        count_product = req.POST.get("count_product", False)
        category_product = req.POST.get("category_product", False)
      

        if False in [name_product, price_product, count_product, category_product, id_cat]:
            return redirect("product")

        s_c = subcategories.objects.get(name=category_product)

        p = products.objects.get(id=id_cat)
        p.name = name_product
        p.price = int(price_product)
        p.count = int(count_product)
        p.category = s_c
        p.save()
       
        return redirect("product")
    elif req.method == "GET":
        if not id_cat:
            redirect("product")
        p = products.objects.filter(id=id_cat, deleted=False)
        if len(p) == 1:
            list_of_product = []
            for i in p:
                list_of_product.append([i.name, i.count, i.price, i.category.name, i.id])

            return render(req, "product/edit.html", {"list": list_of_product})
    raise Http404("محصول یافت نشد")

def get_subcategories(req):

    if req.method == "POST":
        category_product = int(req.POST.get("category_product",1))

        from .models import subcategories , categories
        cat = categories.objects.get(id=category_product)
        s_c = subcategories.objects.filter(parent=cat)
        dict_exp = []
        for sub_cat in s_c:
            dict_exp.append({"id":sub_cat.id,"name":sub_cat.name})
        return JsonResponse(dict_exp,safe=False)
    raise Http404("مجصول یافت نشد")

def get_product(req,id_product):
        if req.user.is_authenticated:
            log = True
        else:
            log = False
        p = products.objects.get(id=id_product)
        product_info = [p.name,p.price,p.count,p.category.name,id_product,p.picture.url]
        return render(req,"product/info.html",{"info":product_info,"log":log})

def category(req):
    if req.user.is_authenticated:
        log = True
    else:
        log = False
        
    c = categories.objects.all()
    cat = []
    
    for i in c:
        sub = subcategories.objects.filter(parent=i)
        subs = []
        for s in sub:
            subs.append([s.name,s.id])
        cat.append([i.id,i.name,subs,i.picture.url])
        
            
    
    return render(req,"product/categories.html",{"categories": cat,"log":log})



def subProducts(req,id_sub):
    if req.user.is_authenticated:
        log = True
    else:
        log = False
    
    p = products.objects.filter(category=subcategories.objects.get(id=id_sub),deleted=False)
    
    c = subcategories.objects.get(id=id_sub)
    id_cat = c.parent.id
    pros = []
    for i in p:
        pros.append([i.name,i.category.name,i.price,i.id,i.picture.url])
    
    return render(req,"product/subProducts.html",{"products":pros,"id_cat":id_cat,"log":log})


