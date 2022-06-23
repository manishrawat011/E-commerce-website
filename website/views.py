from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.products import Product
from .models.categorys import Category
from .models.customers import Customer


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    data= {}
    data['products'] = products
    data['categories']= categories
    return render(request, 'index.html', data)

def signup(request):
    if request.method == 'GET': 
         return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name =  postData.get('firstname')
        last_name =  postData.get('firstname')
        phone = postData.get('phone')
        Email = postData.get('Email')
        password = postData.get('password')
        print(first_name, last_name, phone, Email, password)
        customers = Customer(first_name=first_name, 
                            last_name= last_name, 
                            phone= phone, 
                            email= Email, 
                            password= password)
    
        customers.save()
        return redirect('index')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email= request.POST.get('email')
        password=  request.POST.get('password')
        print(email , password)
        return HttpResponse(request, 'login.html')


