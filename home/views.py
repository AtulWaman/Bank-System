from django.shortcuts import render, HttpResponse
from .models import Customer
def index(request):
    #return HttpResponse("this is Home page "
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("this is About page ") 
    return render(request, 'about.html')   

def services(request):
    # return HttpResponse("this is services page ")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("this is contact page ")
    return render(request, 'contact.html')   

def allcustomers(request):
    # context = {
    #     "variable1":10000
    # }
    # return HttpResponse("this is all customers page ")   
    cx_list=Customer.objects.all()
    # print(cx_list.values)
    return render(request, 'allcustomers.html',context={"cx_list":cx_list.values()})

def perticular_cust(request):
    # return HttpResponse("this is all customers page ")   
    return render(request, 'perticular_cust.html')

# def trans(request):
#     # return HttpResponse("this is all customers page ")   
#     return render(request, 'trans.html')

# views.py

# from django.shortcuts import redirect
# from django.http import HttpResponse
# from .models import Account

# def transfer_money(request):
#     if request.method == 'POST':
#         customer_id = request.POST.get('Customer')
#         amount = request.POST.get('Amount')
        
#         # Perform money transfer logic here
        
#         return HttpResponse("Money transferred successfully!")
    
#     return render(request, 'transfer_money.html', {'Customer': Customer})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Account, Customer, Transfer_money

def transfer_money(request):
    if request.method == 'POST':
        customer_id = request.POST.get('Customer')
        amount = request.POST.get('amount')
        
        sender = Customer.objects.get(cx_id=customer_id)
        sender_firstname = sender.firstname
        sender_lastname = sender.lastname
        
        # Perform money transfer logic here
        # Update sender's account balance and create a Transfer record
        
        Transfer_money.objects.create(sender_firstname=sender_firstname, sender_lastname=sender_lastname, cx_id=sender, amount=amount)
        
        return redirect('allcustomers')
    
    return render(request, 'transfer_money.html', {'customers': Customer.objects.all()})

