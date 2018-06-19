from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField(widget=forms.PasswordInput)
    password3 = forms.CharField(required=False, widget=forms.HiddenInput())
    

    


    
        