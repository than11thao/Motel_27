from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView,TemplateView
from .forms import *
from django.urls import reverse
from Room.models import Room 
from User.models import Renter
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ManageRoomSite(LoginRequiredMixin,TemplateView):
    template_name="manage_room/dashboard.html"
    login_url='home:login'
    def get_context_data(self):
        context=super().get_context_data()
        all_room=Room.objects.all()
        context['all_room']=all_room
        return context

def delete_room(self,id):
    Room.objects.get(room_id=id).delete()
    return redirect("room:manage_room")

class AddRoomSite(LoginRequiredMixin,FormView):
    template_name='home/add_room.html'
    login_url='home:login'
    form_class=AddRoomForm    
    
    def form_valid(self,form):
        Room.objects.create(**form.cleaned_data)
        # print(form.cleaned_data)
        return redirect(reverse("home:dashboard"))
    

    
class EditRoom(LoginRequiredMixin,TemplateView):
    template_name="manage_room/edit_room.html"
    login_url='home:login'
    edit_room_form=EditRoomForm
    context={}
    def get(self, request,id, *args, **kwargs):
        room=Room.objects.get(room_id=id)
        return self.render_to_response(self.get_context_data(room))
    
    
    def get_context_data(self,room_instance):
        context= super().get_context_data()
        context['room']=room_instance
        initial_form_data = {
            "room_number" :room_instance.room_number,
            "area" : room_instance.area,
            "room_price":room_instance.room_price,
            "status":True,
            "description":room_instance.description
        }
        context['edit_room_form']=self.edit_room_form(initial=initial_form_data)
        self.context.update(context)
        return context
    
    
    def post(self,request,id):
        room=self.context['room']
        form=self.edit_room_form(request.POST or None,instance=room)
        if form.is_valid():
            form.save()
            return HttpResponse("thanh cong")
        # else:
        #     return HttpResponse("that bai")
        return HttpResponse("4")
    


class AddMemberRoom(LoginRequiredMixin,TemplateView):
    template_name="manage_room/add_member.html"
    login_url='home:login'
    # add_member_form=AddMemberRoomForm
    context={}
    def get_context_data(self,id):
        context=super().get_context_data()  
        context['add_member_form']=AddMemberRoomForm()
        context['room']=Room.objects.get(room_id=id)
        self.context.update(context)
        return context
    
    def post(self,request,id):
        user_id=request.POST.get('member_id')
        if Renter.objects.filter(user__id=user_id).exists():
            return HttpResponse("exists member in another room")
        room=self.context['room']
        
        if not room.status:
            room.status=True
            room.save()
        
        Renter.objects.create(
            user=MyUser.objects.get(id=user_id),
            room=self.context['room'],
            citizen_id=request.POST.get('citizen_id')
        )
        return redirect("room:manage_room")
        