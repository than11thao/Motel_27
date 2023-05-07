from django.urls import path,include
from .import views
app_name="user"
urlpatterns = [
    path('dashboard/', views.ManageRenterSite.as_view(), name = "manage_user"),
    path('edit_renter/<str:renter_id>/', views.EditRenterSite.as_view(),name = "edit_renter"),
    path('delete_user/<str:id>/',views.delete_user, name = "delete_renter"),
    path('provide_account_user/', views.ProvideAccountUser.as_view(),name="provide_account_user"),
    path('edit_user_of_renter_site/<str:id>/', views.Edit_user_of_renter_site.as_view(), name="edit_user_of_renter_site")
]   
