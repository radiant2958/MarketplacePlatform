from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Product

class SellerSignUpForm(UserCreationForm):
    company_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'company_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        user.company_name = self.cleaned_data['company_name']
        if commit:
            user.save()
        return user

class BuyerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_buyer = True
        if commit:
            user.save()
        return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']