from django.shortcuts import render

from django.http.response import HttpResponse

from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Prefetch
from django.db.models import Q
import random
from webapp.models import Product,Image,Review
from django.core.paginator import Paginator
from django.db.models import Min
from django.http import HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.db.models.functions import Round
from django.db.models import Avg
from time import sleep

def image_upload_view(request):

    if request.method == 'POST':

            name=request.POST["name"]
            description=request.POST["description"]
            category=request.POST["category"]
            price=request.POST["price"]
            try:
                pimg=request.FILES["photo"]
            except:
                pimg=""
            if name=="":
                formvalid="Ürün ismi gerekli"
                return render(request,"addproduct.html",{"form": formvalid})
            elif price=="":
                formvalid="Ürün fiyatı gerekli"
            elif description=="":
                formvalid="Ürün açıklaması gerekli"
            elif category=="":
                formvalid="Ürün kategorisi gerekli"
            elif pimg=="":
                formvalid="En az bir görsel gerekli"

            foo_instance = Product.objects.create(productname=name, productdesc=description,productprice=price, productcategory=category,productimage=pimg, productseller=request.user)

            
            dictfile={}
            
            for i in range(2,6):
                try:
                    image=request.FILES["images"+str(i)]


                    if image.size>3000000:
                        err="Boyutu 3MB'dan büyük dosya yüklediniz."
                        return render(request, 'addproduct.html', {'err': err})
                    dictfile["image"+str(i)]=image
                except:continue

            if len(dictfile)!=0:

                for i in dictfile:
                    Image.objects.create(image=dictfile[i], product_id=foo_instance.id)
 
            """
            try:
                image1=request.FILES["images1"]
                Image.objects.create(image=image1, product_id=foo_instance.id)
        
                for i in range(2,6):
                    try:
                        Image.objects.create(image=request.FILES["images"+str(i)], product_id=foo_instance.id)
                    except:
                        break
    
            except:
                return render(request, 'addproduct.html',{"err":"Ürün görseli eklenmedi"})

            """
            images = Image.objects.all()
            return render(request, 'addproduct.html', {'images': images})
 
    return render(request, 'addproduct.html')
def index(request):

    return render(request,"index.html")


def register(request):
    rdata={} 
    if request.method =="POST":
        
        username= request.POST["username"]
        password= request.POST["password"]
        password2= request.POST["password2"]
        email= request.POST["email"]
        if len(username)<5:

            rdata["error"]="kullanıcı adınız 5 haneden kısa"
        if len(password)<8:
            rdata["error"]="Şifreniz 8 haneden kısa"
        elif User.objects.filter(username=username).exists():
            rdata["error"]="Kullanıcı adı kullanımda."
        else:
            user =User.objects.create_user(username=username,email=email,password=password)
            user.save()
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect("/index")
    
    return render(request,"register.html",rdata)


def Login(request):
    rdata={}
    if request.method =="POST":
        
        username= request.POST["username"]
        
        password= request.POST["password"]
        if len(username)==0:
            rdata["error"]="Kullanıcı adı boş bırakılamaz."
        if len(password)==0:
            rdata["error"]="Şifre boş bırakılamaz."
        else:
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect("/index")
            else:
                rdata["error"]="Kullanıcı adı veya şifre yanlış."
    return render(request,"login.html",rdata)

def addproduct(request):

    if request.user.is_authenticated:
        return render(request,"addproduct.html")
    else:
        return render(request,"index.html")
        
def testing(request):
    ddd=Review.objects.all()
    for prd in ddd:
        prd.delete()

    return render(request,"index.html")
"""
def testing(request):
         
        z=0
        for i in range(1,200000):
            print(i)
            #Review.objects.create(comment="Deneme ürünü gdfgdfg wsd fsdf sdfsdfsd",rating=random.randrange(1,6),product=i)
            z+=1
            if z==16:
                z=1

            Product.objects.create(productname="Deneme ürünü "+str(i),productprice=random.randrange(15000,45000),productcategory="Telefon",productdesc="wsadffs",productimage="images/"+str(z)+".jpg",productseller=request.user)

               
            print(i)
        return render(request,"index.html")
        
"""
"""
def testing(request):
        return render(request,"index.html")
        y=0
        prd=Product.objects.all()[2:6]
        while True:
            for i in prd:
                print(i)

                y+=1
                rate=random.randrange(1,6)
                Review.objects.create(comment="Deneme ürünü gdfgdfg wsd fgdf ghdfg dfg dfsdf sdfsdfsd",rating=5,product=i)
                i.addstar(5)
                print(y)
        return render(request,"index.html")
"""

def ajaxlist(request):
    if request.method == "GET":
        page_number = request.GET.get("cpage")
        searchtext=request.GET.get("searchtext")
        print(page_number)
        if page_number=="":
            page_number = 1
            
        else:
            try:
                page_number = int(page_number)
            except:
                page_number=1   
        offset=(page_number-1) * 16 # product per page

        page_obj=list(Product.objects.filter(productname__icontains=searchtext)[offset:offset+16].values("productname","productprice","productimage","productrating","productratingcount","slug"))

        #page_obj=Product.objects.annotate(rating = Avg("review__rating")).order_by('-rating')
        #page_obj=Product.objects.filter(id__gt=8910)[:16]
        #page_obj2=serializers.serialize("json",page_obj)


 
        # if nick_name found return not valid new friend

        return JsonResponse({"object":page_obj} )
        
    else:
        # if nick_name not found, then user can create a new friend.
        return JsonResponse({"valid":True}, status = 200)
    
    if page_number.isdigit():
        page_number = int(page_number)
    else: page_number = 1
    offset=(page_number-1) * 16 # product per page
    page_obj=Product.objects.filter(productname__icontains="fgjhrdg")[offset:offset+16]
    #page_obj=Product.objects.filter(id__gt=8910)[:16]
    return render(request,"listing.html",{"products": page_obj})







def listview(request):
    
    #products=Product.objects.filter(productname="")


    
    #products=Product.objects.raw("SELECT * FROM 'webapp_product' WHERE productname=''")
    

    #products2=Image.objects.select_related("product").all()
    #products=Product.objects.all().prefetch_related('image_set')
    #print(products2[1].image_set.all()[0].image) 

    #product5 = Product.objects.prefetch_related(
    #        Prefetch("image_set",          
    #        queryset=Image.objects.select_related("product"))).get(pk=1)
    #print(product5.image_set.all().first().image)


    
    
    #products3=Image.objects.values("product").annotate(id=Min("id"))
 
    page_number = request.GET.get("page")

    if page_number=="":
        page_number = 1
        
    else:
        try:
            page_number = int(page_number)
        except:
            page_number=1
    offset=(page_number-1) * 16 # product per page
    page_obj=Product.objects.all()[offset:offset+16].values("productname","productprice","productimage","productrating","productratingcount","slug")
    #page_obj=Product.objects.annotate(rating = Avg("review__rating"))[:16].values("productname","productprice","productimage","rating")
    
    #page_obj=Product.objects.filter(id__gt=8910)[:16]
    return render(request,"listing.html",{"products": page_obj})



def listview_with_pagination(request):
    products=Product.objects.all()
    #products=Product.objects.filter(productname="")
    print(products)

    
    #products=Product.objects.raw("SELECT * FROM 'webapp_product' WHERE productname=''")
    

    products=Product.objects.all().prefetch_related('image_set')
    #print(products2[1].image_set.all()[0].image)

    products = page_obj=Product.objects.filter(productcategory="Telefon",productname__contains="galaxy s6").annotate(Avg("review__set")).values("productname","productprice","productimage","productrating","productratingcount")
    
    #        Prefetch("image_set",          
    #        queryset=Image.objects.select_related("product"))).get(pk=1)
    #print(product5.image_set.all().first().image)

    i=0

    
    
    #products3=Image.objects.values("product").annotate(id=Min("id"))
 

    p = Paginator(products, 16)
    page_number = request.GET.get("page")

    page_obj = p.get_page(page_number)
    return render(request,"listingnew.html",{"products": page_obj})



def review(request):
    #page_obj=Product.objects.annotate(rating = Avg("review__rating")).order_by('-rating')
    #print(page_obj.get(id=53354).rating)
    if request.method == 'POST':

        pname=request.POST["name"]
        comment=request.POST["description"]
    
        cstar=int(request.POST["price"])

        prd=Product.objects.get(productname=pname)
        prd.addstar(cstar)
        foo_instance = Review.objects.create(comment=comment, rating=cstar, product=prd)
       
    return render(request,"addrev.html")




def productpage(request,slug):

    #product=Product.objects.prefetch_related('image_set').get(slug=slug)
    #print(product)

    return render(request,"product.html")

def listtest(request):
    
    #products=Product.objects.filter(productname="")


    
    #products=Product.objects.raw("SELECT * FROM 'webapp_product' WHERE productname=''")
    

    #products2=Image.objects.select_related("product").all()
    #products=Product.objects.all().prefetch_related('image_set')
    #print(products2[1].image_set.all()[0].image) 

    #product5 = Product.objects.prefetch_related(
    #        Prefetch("image_set",          
    #        queryset=Image.objects.select_related("product"))).get(pk=1)
    #print(product5.image_set.all().first().image)


    
    
    #products3=Image.objects.values("product").annotate(id=Min("id"))
 
    page_number = request.GET.get("page")

    if page_number=="":
        page_number = 1
        
    else:
        try:
            page_number = int(page_number)
        except:
            page_number=1
    offset=(page_number-1) * 16 # product per page
    page_obj=Product.objects.filter()[offset:offset+16].values("productname","productprice","productimage","productrating","productratingcount","slug")
    #page_obj=Product.objects.annotate(rating = Avg("review__rating"))[:16].values("productname","productprice","productimage","rating")
    
    #page_obj=Product.objects.filter(id__gt=8910)[:16]
    return render(request,"listtest.html",{"products": page_obj})


def search(request):
    
    #products=Product.objects.filter(productname="")


    
    #products=Product.objects.raw("SELECT * FROM 'webapp_product' WHERE productname=''")
    

    #products2=Image.objects.select_related("product").all()
    #products=Product.objects.all().prefetch_related('image_set')
    #print(products2[1].image_set.all()[0].image) 

    #product5 = Product.objects.prefetch_related(
    #        Prefetch("image_set",          
    #        queryset=Image.objects.select_related("product"))).get(pk=1)
    #print(product5.image_set.all().first().image)


    
    
    #products3=Image.objects.values("product").annotate(id=Min("id"))
    searchtext=request.GET.get("q")
    page_number = request.GET.get("page")

    if page_number=="":
        page_number = 1
        
    else:
        try:
            page_number = int(page_number)
        except:
            page_number=1
    offset=(page_number-1) * 16 # product per page
    page_obj=Product.objects.filter(productname__icontains=searchtext)[offset:offset+16].values("productname","productprice","productimage","productrating","productratingcount","slug")
    #page_obj=Product.objects.annotate(rating = Avg("review__rating"))[:16].values("productname","productprice","productimage","rating")
    
    #page_obj=Product.objects.filter(id__gt=8910)[:16]
    return render(request,"listing.html",{"products": page_obj})


def stack(request):
    if request.method =="POST":
        
        departure = request.GET.get("idofselect").split("-")[0]
    return render(request,"sdasf.html")