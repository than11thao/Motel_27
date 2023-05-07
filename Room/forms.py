from django import forms
from .models import Room
from User.models import MyUser
# from User.models import MyUser
class AddRoomForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Room
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control',})


class EditRoomForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Room
        fields = ['room_number', 'area', 'room_price', 'status','description',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})


class AddMemberRoomForm(forms.Form):
    member_id = forms.MultipleChoiceField()
    citizen_id = forms.CharField(max_length=15)

    def __init__(self,*args,**kwargs):
        print("init ::::::::::")
        super().__init__(*args,**kwargs)
        arr_user= []
        for user in MyUser.objects.all():
            if hasattr(user,'renter') == False:
                arr_user.append(user)
            
        list_member = [(user.id, "ID : {} - {}".format(user.id,user.full_name)) for user in arr_user ]
        self.fields['member_id'] = forms.ChoiceField(choices=list_member)
        self.fields['member_id'].widget.attrs.update({'class':'form-control'})
        self.fields['citizen_id'].widget.attrs.update({'class':'form-control'})

