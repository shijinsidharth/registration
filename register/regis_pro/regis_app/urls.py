from os import name
from django.urls import path
from.import views
urlpatterns=[
    path('test',views.Testfn,name="new"),
    path('html1',views.html1,name="html1"),
    path('reg',views.reg1,name="reg"),
    path('view_users',views.views1,name="view_users"),
    path('login',views.login,name="login"),
    path('home',views.home,name="home"),
    path('profile',views.profile,name="profile"),
    path('update',views.update,name="update"),
    path('insert',views.insert,name="insert"),
    path('show',views.show,name="show"),
    path('logout',views.logout,name="logout"),
    path('json',views.json,name="json"),
    # path('checkusername',views.checkusername,name="checkusername")
]