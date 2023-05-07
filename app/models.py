from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
STATE_CHOICES = (
    ('Bagmati Province','Bagmati Province'),
    ('Gandaki Province', 'Gandaki Province'),
    ('Karnali Province', 'Karnali Province'),
    ('Lumbini Province','Lumbini Province'),
    ('Madhesh Province', 'Madhesh Province'),
    ('Province 1', 'Province 1'),
    ('Sudurpashchim Province', 'Sudurpashchim Province'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=13,default='')
    locality = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

def __str__(self):
    return str(self.id)

CATEGORY_CHOICES = (
    ('breads', 'Bread'),
    ('cakes', 'Cake'),
    ('cupcakes', 'Cupcake'),
    ('cookies', 'Cookies'),
    ('dessert', 'Dessert'),
    ('doughnuts', 'Doughnut'),
    ('pastries', 'Pastries'),
    ('todayspecial', 'Featured'),
    ('specialoffer1', 'Specialoffer1'),
    ('specialoffer2', 'Specialoffer2'),
    ('specialoffer3', 'Specialoffer3'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)
    product_image = models.ImageField(upload_to='productsimg')

def __str__(self):
    return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price