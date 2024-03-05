
from django.urls import path
from . import views


app_name = "fresh_tohome"

urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("sproduct/", views.sproduct, name="sproduct"),
    path("about_farmers/", views.about_farmers, name="about_farmers"),
    path("about_us/",views.about_us, name="about_us"),
    path("contact",views.contact, name="contact"),
    path("cart",views.cart,name="cart"),
    path("offers",views.offers,name="offers"),
    path("sign_up",views.sign_up,name="sign_up"),
    path("sign_in", views.sign_in, name="sign_in")
]
