from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name="home"),
    path('home',views.Home, name="home"),
    path('register',views.Register_fun,name="register"),
    path('login',views.login_fun,name="login"),
    path('contact',views.contactus_fun,name="contact"),
    path('about',views.aboutus_fun,name="about"),
    path('logout',views.logout_fun,name="logout"),
    path('userdashboard',views.user_dashboard,name="userdashboard"),
    path('update/<int:id>',views.update_fun,name="update"),
    path('delete/<int:id>',views.delete_fun,name="delete"),
     #url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]
