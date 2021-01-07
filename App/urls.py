from django.urls import path
from App import views
from django.urls import path
from django.contrib.auth import views as g

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('ap/',views.products,name="pro"),
	path('vege/',views.vegetables,name="veg"),
	path('fru/',views.fruits,name="fit"),
	path('da/',views.dairy,name="day"),
	path('pu/',views.pulses,name="pul"),
	path('ho/',views.house,name="hom"),
	path('po/',views.care,name="car"),
	path('ca/',views.cart,name="cat"),
	path('cnt/',views.contact,name="ct"),
	path('rg/',views.register,name="reg"),
	path('pf/',views.prfle,name="pfe"),
	path('upf/',views.updf,name="upfe"),
	path('lg/',g.LoginView.as_view(template_name="html/login.html"),name="lgn"),
	path('lgg/',g.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]
