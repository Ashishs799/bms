
from jet.dashboard.modules import DashboardModule
from django.db.models import Sum
from app.models import OrderPlaced,Product, Customer, Cart
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string


class TotalOrdersWidget(DashboardModule):
    title = 'Total Orders'

    def render(self, request=None):
        total_orders = OrderPlaced.objects.all().count()
        context = {
            'total_orders': total_orders,
        }
        return render_to_string('widgets/total_orders.html', context)

class TotalUserWidget(DashboardModule):
    title = 'Total Users'

    def render(self, request=None):
        User = get_user_model()
        total_users = User.objects.all().count()
        context = {
            'total_users': total_users,
        }
        return render_to_string('widgets/total_users.html', context)


class TotalProductWidget(DashboardModule):
    title = 'Total Products'

    def render(self, request=None):
        total_products = Product.objects.all().count()
        context = {
            'total_products': total_products,
        }
        return render_to_string('widgets/total_products.html', context)

class TotalCustomerWidget(DashboardModule):
    title = 'Total Customers'

    def render(self, request=None):
        total_customers = Customer.objects.all().count()
        context = {
            'total_customers': total_customers,
        }
        return render_to_string('widgets/total_customers.html', context)
#
#
class TotalCartWidget(DashboardModule):
    title = 'Total Carts'

    def render(self, request=None):
        total_carts = Cart.objects.all().count()
        context = {
            'total_carts': total_carts,
        }
        return render_to_string('widgets/total_carts.html', context)

class TotalSalesWidget(DashboardModule):
    title = 'Total Sales'

    def render(self, request=None):
        orders = OrderPlaced.objects.all()
        total_sales = 0
        for order in orders:
            total_sales += int((order.product.discounted_price * order.quantity)) or 0
        context = {
            'total_sales': total_sales,
        }
        return render_to_string('widgets/total_sales.html', context)


class BarChartWidget(DashboardModule):
    title = 'Sales Overview'

    def render(self, request=None):
        return render_to_string('widgets/chart.html')
#
# class RecentOrderWidget(DashboardModule):
#     title = 'Recent Orders'
#
#     def render(self, request=None):
#         recent_orders = OrderPlaced.objects.all().order_by('-ordered_date')[:10]# Retrieve the 5 most recent orders from the database
#         context = {'recent_orders': recent_orders} # Create a context dictionary with the recent orders data
#         return render_to_string('widgets/recent_orders.html', context)
#
# class ActionsWidget(DashboardModule):
#     title = 'Recent Actions'
#     def render(self, request=None):
#         return render_to_string('widgets/recent_action.html')