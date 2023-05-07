from django import forms
from .models import Bill
from .models import Room

class CreateBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'

    def __init__(self,*args, **kwards):
        super().__init__(*args, **kwards)
        self.fields['room'] = forms.ModelChoiceField(queryset=Room.objects.filter(status= True))
        self.fields['date'].label = "Date Format(mm/dd/yyyy)"
        self.fields['date'].widget = forms.DateInput(format='%d/%m/%Y')
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control',})

    def clean_electricity_price(self):
        if self.cleaned_data['electricity_price'] < 0:
            raise forms.ValidationError("Điện < 0")
        return self.cleaned_data['electricity_price']
    

class EditBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control',})
        self.fields['date'].label = "Date Format(dd/mm/yyyy)"
        self.fields['room'].widget = forms.HiddenInput()
