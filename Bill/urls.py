from django.urls import path,include
from . import views
app_name="bill"
urlpatterns = [
    path('dashboard/', views.BillSite.as_view(), name = "bill_site"),
    path('dashboard/<str:month>/', views.BillSite.as_view(),name="bill_site_with_month"),
    path('edit_bill/<str:id>/', views.EditBillSite.as_view(), name = "edit_bill"),
    path('delete_bill/<str:id>/', views.delete_bill, name= "delete_bill"),
    path('bill_of_renter_site/', views.BillOfRenterSite.as_view(),name="bill_of_renter_site"),
    path('bill_of_renter_site/<str:date>/', views.BillOfRenterSite.as_view(),name="bill_with_id_of_renter_site")

]   
