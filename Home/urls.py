from django.urls import path
from .import views
app_name="home"

urlpatterns = [
    path('login/', views.LoginSite.as_view(), name ='login'),
    path('logout/', views.LogOut, name = 'logout'),
    path('dashboard/',views.DashBoardSite.as_view(), name="dashboard"),
    path('renter_site/', views.RenterDashBoardSite.as_view(), name="renter_site"),
    path('register/',views.SignupPage, name= 'signup'),
]
