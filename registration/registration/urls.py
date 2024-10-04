from django.contrib import admin
from django.urls import path
from app1 import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name="login"),
    path('home/',views.home,name='logout'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Accounts/', views.account, name='account'),
    path('dashboard_user/',views.user_dash , name= 'dashboard_user'),
    path('Delete_users/(?P<pk>\d+)/',views.Deleteuser,name='Delete'),
    path('update/(?P<pk>\d+)/',views.update,name='update'),
    path('update_users/(?P<pk>\d+)/', views.updateuser, name='updateuser'),
    path('updatprofile/(?P<pk>\d+)/', views.updatprofile, name='updatprofile'),
    path('add_user/',views.AddUser,name='add_user'),
    path('verify/(?P<pk>\d+)/',views.verify_user,name='verify'),
    path('gett/',views.get_all_person),


]
