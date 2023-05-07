from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
=======

urlpatterns = [
>>>>>>> adabc05409fff91934323e19406acf814d1e1901
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
