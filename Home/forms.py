from django import forms
from Room.models import Room


class AddRoomForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Room
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control',})