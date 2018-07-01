from django import forms

class RegistrationForm(forms.Form):
    First_Name = forms.CharField(label = 'First Name', max_length= 100)
    Last_Name = forms.CharField(label = 'Last Name', max_length= 100)
    Username = forms.CharField(label='Username', max_length=100)
    Email =forms.EmailField(label ='Email')
    Address =forms.CharField(label = 'Address(Street)', max_length=60)
    City = forms.CharField(label='Address(City)', max_length=50)
    Zip_Code =forms.IntegerField(label='Zip Code')
    psw = forms.CharField(widget=forms.PasswordInput, label='Password')
    psw_repeat = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

