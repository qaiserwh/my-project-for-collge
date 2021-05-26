from django.urls import  path
from .import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
urlpatterns = [
     path('',views.books, name='books' ),
     path('login', views.admin_login, name='login'),
     path('index',views.index, name='index' ),
     path('order',views.order, name='order' ),
     path('update/<int:id>',views.update, name='update'),
     path('delete/<int:id>',views.delete, name='delete'),
     path('about_us',views.about, name='about'),
     path('orderdata',views.orderdata, name='orderdata'),
     path('admin/',views.Admin,name="admin/"),
  
 ]