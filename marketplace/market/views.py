from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import logging

from django.urls import reverse

from market.models import CustomUser, Product
from market.forms import BuyerSignUpForm, ProductForm, SellerSignUpForm
logger = logging.getLogger(__name__)


def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_seller:
                return redirect('seller') 
            else:
                return redirect('buyer')  
        else:
            
            messages.error(request, 'Email или пароль неверны.')
            return redirect('login')
    return render(request, 'market/login.html')  



def register(request):
    print("Request method:", request.method)
    print("POST data:", request.POST)
    login(request, user)
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST) if 'seller' in request.POST.get('role', '') else BuyerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'status': 'ok', 'redirect_url': reverse('buyer') if user.is_buyer else reverse('seller')})
        else:
            errors = form.errors.as_data()  
            print(errors)  
            errors_list = [f"{field}: {error[0].message}" for field, error in errors.items()]
            return JsonResponse({'status': 'error', 'errors': errors_list}, status=400)
    else:
        form = SellerSignUpForm() if 'seller' in request.GET.get('role', 'buyer') else BuyerSignUpForm()
    return render(request, 'market/register.html', {'form': form})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return render(request, 'product_added.html', {'product': product})
    else:
        form = ProductForm()
    return render(request, 'market/add_product.html', {'form': form})

def buyer_dashboard(request):
    products = Product.objects.all()
    return render(request, 'matket/buyer.html', {'products': products})


def index(request):
    return render(request, "market/index.html")

def seller(request):
    return render(request, "market/seller.html")

def buyer(request):
    return render(request, "market/buyer.html")

def add_product(request):
    return render(request, "market/add_product.html")

def product_added(request):
    return render(request, "market/product_added.html")

def login(request):
    return render(request, "market/login.html")

def register(request):
    return render(request, "market/register.html")

