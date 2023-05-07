from django import forms
from .models import *
from Room.models import Room


class EditRenterForm(forms.Form):
    list_room = [(room.room_id, "Room number1 : {}".format(room.room_number)) for room in Room.objects.all()]
    citizen_id = forms.IntegerField()

    def __init__(self, request, *args, **kwards):
        super().__init__(*args, **kwards)
        if request.user.is_owner:
            self.fields["room_id"]= forms.ChoiceField(choices=self.list_room)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})


class EditUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['full_name', 'phone_number', 'email', 'address', 'is_active']

    def __init__(self, request, *args , **kwargs):
        super().__init__(*args, **kwargs)
        if not request.user.is_owner:
            self.fields["is_active"].widget = forms.HiddenInput()

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class AddUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username','email', 'email','full_name', 'phone_number', 'address', 'is_active']

    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})