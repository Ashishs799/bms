from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):
 def get(self, request):
  totalitem = 0
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
  if request.user.is_authenticated:
   totalitem = len(Cart.objects.filter(user=request.user))
  return render(request, 'app/home.html', {'Bread': Bread, 'Cake' : Cake, 'Cupcake': Cupcake, 'Cookies': Cookies,
  'Dessert': Dessert, 'Doughnut': Doughnut, 'Pastries': Pastries, 'Featured':Featured, 'Specialoffer1':Specialoffer1, 'Specialoffer2':Specialoffer2,'Specialoffer3':Specialoffer3, 'totalitem':totalitem})


class ProductDetailView(View):
 def get(self, request, pk):
  totalitem = 0
  product = Product.objects.get(pk=pk)
  item_already_in_cart = False
  item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
  if request.user.is_authenticated:
   totalitem = len(Cart.objects.filter(user=request.user))
  return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart, 'totalitem':totalitem})
@login_required
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 page = request.GET.get('page')

 # Check if the user already has a cart item for this product
 cart_item = Cart.objects.filter(user=user, product=product).first()
 if cart_item:
  # If the item already exists, increase the quantity by 1
  cart_item.quantity += 1
  cart_item.save()
 else:
  # If the item doesn't exist, create a new cart item with quantity 1
  Cart(user=user, product=product, quantity=1).save()

 # Redirect to the appropriate page
 if page == 'home':
  return redirect('/')
 else:
  return redirect('/cart')


@login_required
def show_cart(request):
 totalitem = 0
 if request.user.is_authenticated:
  totalitem = len(Cart.objects.filter(user=request.user))
  user = request.user
  cart = Cart.objects.filter(user=user)
  # print(cart)
  amount = 0.0
  shipping_amount = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user==user]
  # print(cart_product)
  if cart_product:
   for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount
    total_amount = amount + shipping_amount
   return render(request, 'app/addtocart.html', {'carts':cart, 'total_amount':total_amount, 'amount':amount,'totalitem':totalitem})
  else:
   return render(request,'app/emptycart.html',{'totalitem':totalitem})

# To increase quantity of product in cart
def plus_cart(request):
 if request.method == 'GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity += 1
  c.save()

  amount = 0.0
  shipping_amount = 70.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount

  data = {
    'quantity': c.quantity,
    'amount':amount,
    'total_amount':amount + shipping_amount
    }
  return JsonResponse(data)

# To decrease quantity of Products in cart
def minus_cart(request):
 if request.method == 'GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity -= 1
  c.save()
  amount = 0.0
  shipping_amount = 70.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount

  data = {
    'quantity': c.quantity,
    'amount':amount,
    'total_amount':amount + shipping_amount
    }
  return JsonResponse(data)

def remove_cart(request):
 if request.method == 'GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.delete()
  amount = 0.0
  shipping_amount = 70.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount

  data = {
    'amount':amount,
    'total_amount':amount + shipping_amount
    }
  return JsonResponse(data)
def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')
@login_required
def address(request):
 totalitem = 0
 add = Customer.objects.filter(user=request.user)
 if request.user.is_authenticated:
  totalitem = len(Cart.objects.filter(user=request.user))
 return render(request, 'app/address.html',{'add':add,'active':'btn-outline-info','totalitem':totalitem})
@login_required
def orders(request):
 totalitem = 0
 op = OrderPlaced.objects.filter(user=request.user)
 if request.user.is_authenticated:
  totalitem = len(Cart.objects.filter(user=request.user))
 return render(request, 'app/orders.html',{'order_placed':op,'totalitem':totalitem})


# def change_password(request):
#  return render(request, 'app/changepassword.html')

def about(request):
 totalitem = 0
 if request.user.is_authenticated:
  totalitem = len(Cart.objects.filter(user=request.user))
 return render(request, 'app/about.html',{'totalitem':totalitem})

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
@login_required
def checkout(request):
 totalitem = 0
 if request.user.is_authenticated:
  totalitem = len(Cart.objects.filter(user=request.user))
  user = request.user
  add = Customer.objects.filter(user=user)
  cart_items = Cart.objects.filter(user=user)
  amount = 0.0
  shipping_amount = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  if cart_product:
   for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount
   total_amount = amount+shipping_amount
 return render(request, 'app/checkout.html', {'add':add, 'total_amount':total_amount,'cart_items':cart_items,'totalitem':totalitem})

@login_required
def payment_done(request):
 totalitem = 0
 if request.user.is_authenticated:
  totalitem = len(Cart.objects.filter(user=request.user))
  user = request.user
  custid = request.GET.get('custid')
  customer = Customer.objects.get(id=custid)
  cart  = Cart.objects.filter(user=user)
  for c in cart:
   OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
   c.delete()
 return redirect(f"/orders/?totalitem={totalitem}")
 # return redirect("orders",{'totalitem':totalitem})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
 def get(self,request):
  totalitem = 0
  if request.user.is_authenticated:
   totalitem = len(Cart.objects.filter(user=request.user))
   form = CustomerProfileForm()
  return render(request,'app/profile.html',{'form':form, 'active':'btn-outline-info','totalitem':totalitem})

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