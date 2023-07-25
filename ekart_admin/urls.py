from django.urls import path
from. import views

app_name = "ekart_admin"

urlpatterns = [   
   path('admin_home',views.admin_home,name="admin_home"),
   path('add_category',views.add_category,name="add_category"),
   path('view_category',views.view_category,name="view_category"),
   path('pending_sellers',views.pending_sellers,name="pending_sellers"),
   path('approved_sellers',views.approved_sellers,name="approved_sellers"),
   path('customers',views.customers,name="customers"),
]