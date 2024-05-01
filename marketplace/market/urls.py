from django.urls import path
from market.views import custom_login, register, add_product, index, seller, buyer, product_added

urlpatterns = [
    path('', index, name='index'),
    path('login/', custom_login, name='login'),
    path('register/', register, name='register'),
    path('seller/', seller, name='seller'),  
    path('buyer/', buyer, name='buyer'),  
    path('add_product/', add_product, name='add_product'),
    path('product_added/', product_added, name='product_added'),
]
