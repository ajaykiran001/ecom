from django.urls import path
from. import views

app_name = "common"

urlpatterns = [   
    path('',views.home, name='home'),  #path for home page
    path('seller_register',views.seller_register, name='seller_register'), 
    path('seller_login',views.seller_login, name='seller_login'), 
    path('customer_signup',views.customer_signup, name='customer_signup'), 
    path('customer_login',views.customer_login, name='customer_login'), 
    path('admin_login',views.admin_login, name='admin_login'), 

]