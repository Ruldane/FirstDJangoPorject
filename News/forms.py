from django import forms
from .models import RegistrationData, Document


class RegistrationForm(forms.Form):
    # call to the file registration.html
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    phone = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Your phone number'}))

 # create a model form to modalform.html
class RegistrationModalForm(forms.ModelForm):
    class Meta:
        model = RegistrationData
        fields = [
            'username',
            'email',
            'password',
            'phone'
        ]
        # to add widget at the model form
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Your phone number'})

        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'description',
            'document',
        ]


