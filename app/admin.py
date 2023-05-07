from django.contrib import admin
<<<<<<< HEAD
from django.utils.html import format_html
from django.urls import reverse

=======
>>>>>>> adabc05409fff91934323e19406acf814d1e1901
from .models import(
Customer,
Product,
Cart,
OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'category', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','quantity','product']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['id','user','customer','customer_info','product','product_info','quantity','ordered_date','status']

    def customer_info(self,obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href = "{}">{}</a>', link, obj.customer.name)

    def product_info(self,obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href = "{}">{}</a>', link, obj.product.title)
=======
    list_display = ['id','user','customer','product','quantity','ordered_date','status']
>>>>>>> adabc05409fff91934323e19406acf814d1e1901
