from django.urls import path
from. import views

app_name = "Seller"

urlpatterns = [   
    path('',views.seller_home,name="seller_home"),
    path('add_product',views.add_product,name="add_product"),
    path('add_category',views.add_category,name="add_category"),
    path('view_product',views.view_products,name="view_product"),
    path('view_category',views.view_category,name="view_category"),
    path('profile',views.profile,name="profile"),
    path('view_orders',views.view_orders,name="view_orders"),
    path('update_stock',views.update_stock,name="update_stock"),
    path('order_history',views.order_history,name="order_history"),

   
]