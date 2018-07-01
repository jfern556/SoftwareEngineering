from django import forms

''' still not functional '''
class QuantityChangeForm(forms.Form):
    New_quantity = forms.IntegerField()
    Cart_contentID = forms.CharField(widget = forms.HiddenInput)
    