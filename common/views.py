from django.shortcuts import render

# Create your views here.


#functon for rendering home page
def home(request):
    return render(request,'common/home.html' )

#function for rendering seller register page
def seller_register(request):
    return render(request,'common/seller_register.html' )

#function for rendering seller login page
def seller_login(request):
    return render(request,'common/seller_login.html' )

#function for rendering customer register page
def customer_signup(request):
    return render(request,'common/customer_signup.html' )

#function for rendering customer login page
def customer_login(request):
    return render(request,'common/customer_login.html' )

def admin_login(request):
    return render(request,'common/admin_login.html' )