from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
 def get(self, request):
  Bread = Product.objects.filter(category = 'breads')
  Cake = Product.objects.filter(category = 'cakes')
  Cupcake = Product.objects.filter(category = 'cupcakes')
  Cookies = Product.objects.filter(category = 'cookies')
  Dessert = Product.objects.filter(category = 'dessert')
  Doughnut = Product.objects.filter(category = 'doughnuts')
  Pastries = Product.objects.filter(category = 'pastries')
  Featured = Product.objects.filter(category = 'todayspecial')
  Specialoffer1 = Product.objects.filter(category = 'specialoffer1')
  Specialoffer2 = Product.objects.filter(category = 'specialoffer2')
  Specialoffer3 = Product.objects.filter(category = 'specialoffer3')
  return render(request, 'app/home.html', {'Bread': Bread, 'Cake' : Cake, 'Cupcake': Cupcake, 'Cookies': Cookies,
  'Dessert': Dessert, 'Doughnut': Doughnut, 'Pastries': Pastries, 'Featured':Featured, 'Specialoffer1':Specialoffer1, 'Specialoffer2':Specialoffer2,'Specialoffer3':Specialoffer3})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'add':add,'active':'btn-outline-info'})

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request,'app/customerregistration.html',{'form':form})
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'You are registered Successfully!!')
   form.save()
  return render(request,'app/customerregistration.html',{'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
 def get(self, request):
  form = CustomerProfileForm()
  return render(request,'app/profile.html',{'form':form})

class ProfileView(View):
 def get(self,request):
  form = CustomerProfileForm()
  return render(request,'app/profile.html',{'form':form, 'active':'btn-outline-info'})

 def post(self,request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
   usr = request.user
   phone = form.cleaned_data['phone']
   name = form.cleaned_data['name']
   locality = form.cleaned_data['locality']
   city = form.cleaned_data['city']
   state = form.cleaned_data['state']
   zipcode = form.cleaned_data['zipcode']
   reg = Customer(user=usr,phone=phone,name=name,locality=locality,city=city,state=state,
                  zipcode=zipcode)
   reg.save()
   messages.success(request,'Congratulations!! Your Profile is updated successfully!!')
  return render(request,'app/profile.html',{'form':form, 'active':'btn-outline-info'})