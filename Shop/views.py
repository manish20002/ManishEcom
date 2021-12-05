from django.http import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil
from datetime import datetime
from Shop.models import Contact, Orders, OrderUpdate
from django.contrib import messages
import json
from django.core.mail import message, send_mail

# Create your views here.
def index (request):
    #products = Product.objects.all()
    #print(products)
    #n = len(products)
    #nslides = n//4 + ceil((n/4)-(n//4))
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nslides), nslides])

    #params ={'no_of_slides':nslides, 'range': range(1,nslides), 'product': products}
    #allProds = [[products, range(1, len(products)), nslides],
    #[products, range(1, len(products)), nslides]]
    params = {'allProds' : allProds} 
    return render(request, 'Shop/index.html', params)

def about (request):
    return render(request, 'Shop/about.html')

def contact (request):
    thank=False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        #contact= Contact(name=name, email=email, desc=desc, date=datetime.today())
        #contact.save()
        #messages.success(request, 'complante has been registard.')
        #thank=True
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            "desc": desc
        }
        print(data)
        messages = '''
        New message: {}

        From: {}
        '''.format(data['desc'], data['email'])
        send_mail(data ['subject'], desc, '', ['pugegamer1@gmail.com'])
    return render(request,'Shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('error')
        except Exception as e:
            return HttpResponse('error')

    return render(request, 'shop/tracker.html')
    
def search (request):
    return render(request, 'Shop/search.html')

def productView(request, myid):
    # fetch the product using the id
    product = Product.objects.filter(id=myid)
    #print("product")
    return render(request, 'Shop/products.html', {'product':product[0]})

def checkout (request):
    if request.method == "POST":
        items_json = request.POST.get('itemsjson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        phone = request.POST.get('phone', '')
        state = request.POST.get('state', '')

        order= Orders(items_Json=items_json, name=name, email=email, city=city, address=address, state=state, phone=phone, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id= order.order_id, update_desc="The Order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'Shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'Shop/checkout.html')



