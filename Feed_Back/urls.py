from django.urls import path
from .import views
app_name="feedback"
urlpatterns = [
    path('feed_back_of_renter/', views.RenterFeedBack.as_view(), name='renter_feed_back'),
]