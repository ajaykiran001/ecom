from django.urls import path
from. import views

app_name = "customer"

urlpatterns = [   
   path('',views.customer_home, name='customer_home'),
   path('store',views.store,name='store'),
   path('product_detail',views.product_detail,name='product_detail'),
   path('cart',views.cart,name='cart'),
   path('place_order',views.place_order,name='place_order'),
   path('order_complete',views.order_complete,name='order_complete'),
   path('dashboard',views.dashboard,name='dasboard'),
   path('seller_register',views.seller_register,name='seller_register'),
   path('seller_login',views.seller_login,name='seller_login'),
   path('customer_signup',views.customer_signup,name='customer_signup'),
   path('customer_login',views.customer_login,name='customer_login'),
   path('forgot_password_customer',views.forgot_password_customer,name='forgot_password_customer'),
   path('forgot_password_seller',views.forgot_password_seller,name='forgot_password_seller'),
   

]