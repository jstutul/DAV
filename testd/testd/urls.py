from django.contrib import admin
from django.urls import path
from testd import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('set',views.setV,name='set'),
]
