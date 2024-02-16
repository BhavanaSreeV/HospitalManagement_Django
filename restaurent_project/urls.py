
from django.contrib import admin
from django.urls import path
from restaurent_app import views
from django.contrib.auth import views as g

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('er/',views.hme,name="hm"),
    path('logn/',g.LoginView.as_view(template_name="firstapp/login.html"),name="lg"),
    path('rgt/',views.rgstr,name="rg"),
    path('bt/',views.btbl,name="tbl"),
    path('py/',views.mnu),
    path('st/',views.abt,name="abt"),
    path('ts/',views.cnct,name="cnt"),
    path('prf/',views.profile,name="prf"),
    path('bok/',views.book,name="book"),
    path('crd/',views.cardio,name="cd"),
    path('neu/',views.neuro,name="neur"),
    path('gstr/',views.gastro,name="gst"),
    path('gync/',views.gynaco,name="gyn"),
    path('Derma/',views.dermo,name="drm"),
    path('update_doc/<int:s>/',views.updt_dct,name="updtdct"),
    path('delete_doc/<int:p>/',views.docdlt,name="dctdel"),

]
