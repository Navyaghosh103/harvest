from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def shop(request):
    return render(request,'shop.html')

def sproduct(request):
    return render(request,'sproduct.html')

def about_farmers(request):
    return render(request,'about_farmers.html')

def about_us(request):
    return render(request,'about_us.html')

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')

def offers(request):
    return render(request,'offers.html')

def sign_up(request):
    return render(request,'sign_up.html')

def sign_in(request):
    return render(request, 'sign_in.html')