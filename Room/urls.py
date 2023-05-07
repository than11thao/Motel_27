from django.urls import path
from .import views
app_name="room"
urlpatterns = [
    path('add_room/', views.AddRoomSite.as_view(), name="add_room"),
    path("manage_room/", views.ManageRoomSite.as_view(), name = "manage_room"),
    path("edit_room/<str:id>/", views.EditRoom.as_view(), name = "edit_room"),
    path("delete_room/<str:id>/", views.delete_room, name="delete_room"),
    path("add_member_room/<str:id>/", views.AddMemberRoom.as_view(), name = "add_member_room"),

]
