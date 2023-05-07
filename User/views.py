from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from User.models import Renter, MyUser
from Room.models import Room
from django.http import HttpResponse
from .forms import EditRenterForm, EditUserForm ,AddUserForm
from django.urls import reverse
# Create your views here.

class ManageRenterSite(TemplateView):
    template_name = 'manage_renter/main.html'

    def get_context_data(self):
        context = super().get_context_data()
        context["renters"] = Renter.objects.all() 
        return context
    

class EditRenterSite(TemplateView):
    template_name = 'manage_renter/edit_renter.html'
    edit_user_form = EditUserForm
    edit_renter_form = EditRenterForm

    def get_context_data(self, renter_id):
        renter = Renter.objects.get(id = renter_id)
        context = super().get_context_data()
        init_edit_user_data = {
            'full_name': renter.user.full_name,
            'phone_number': renter.user.phone_number,
            'email':renter.user.email,
            'full_name': renter.user.full_name,
            'address': renter.user.address
        }
        init_edit_renter_data= {
            'citizen_id': renter.citizen_id
        }
        context['edit_user_form']= EditUserForm(self.request, initial =init_edit_renter_data)
        context['edit_renter_form'] = EditRenterForm(self.request, initial =init_edit_renter_data)
        context['renter'] = Renter.objects.get(id = renter_id)
        return context
    
    def post(self, request, renter_id):
        renter = Renter.objects.get(id = renter_id)
        user = renter.user
        edit_user_form = self.edit_user_form(request, request.POST)
        edit_renter_form = self.edit_renter_form(request, request.POST)

        if edit_renter_form.is_valid() and edit_user_form.is_valid():
            cd_renter = edit_renter_form.cleaned_data
            cd_user = edit_user_form.cleaned_data
            try:
                for field in edit_renter_form.fields:
                    if hasattr(renter, field):
                        if field == "room_id":
                            renter.room = Room.objects.get(room_id = cd_renter['room_id'])
                        else:
                            setattr(renter, field, cd_renter[field])

                for field in edit_user_form.fields:
                    if hasattr(user, field):
                        setattr(user, field,cd_user[field])

                renter.save()
                user.save()

            except:
                return HttpResponse("Lỗi gì đó")
            
        return redirect("user:manage_user")
    
def delete_user(request, id):
    MyUser.objects.get(id = id).detele()
    return redirect("user:manage_user")


class ProvideAccountUser(FormView):
    template_name= "manage_renter/provide_account.html"
    form_class = AddUserForm

    def form_valid(self, form):
        form.save()
        return redirect("user:manage_user")


class Edit_user_of_renter_site(TemplateView):
    template_name="renter_dashboard/partial/edit_user.html"
    edit_user_form = EditUserForm
    edit_renter_form = EditRenterForm

    def get_context_data(self, id):
        context =  super().get_context_data()
        init_edit_user_data = {
            'full_name': self.request.user.full_name,
            'phone_number': self.request.user.phone_number,
            'email': self.request.user.email,
            'address':self.request.user.address,
        }
        renter = Renter.objects.get(id=id)
        init_edit_renter_data={
            'citizen_id':renter.citizen_id
        }
        context['edit_user_form'] = EditUserForm(self.request, initial=init_edit_user_data)
        context['edit_renter_from'] = EditRenterForm(self.request, initial =init_edit_renter_data)
        context['renter'] = Renter.objects.get(id =id)
        return context
    
    def post(self, request, id):
        renter = Renter.objects.get(id = id)
        user = renter.user
        edit_user_form = self.edit_user_form(request, request.POST)
        edit_renter_form = self.edit_renter_form(request, request.POST)

        if edit_user_form.is_valid() and edit_renter_form.is_valid():
            cd_renter = edit_renter_form.cleaned_data
            cd_user = edit_user_form.cleaned_data
            try:
                for field in edit_renter_form.fields:
                    if hasattr(renter, field):
                        if field=="room_id":
                            renter.room = Room.objects.get(room_id=cd_renter['room_id'])
                        else:
                            setattr(renter, field, cd_renter[field])
                for field in edit_user_form.fields:
                    if hasattr(user, field):
                        setattr(user, field, cd_user[field])
                
                renter.save()
                user.save()

            except:
                return HttpResponse("Lỗi gì đó")
            
        url = reverse("user:edit_user_of_renter_site", args=[id])
        return redirect(url)

    
