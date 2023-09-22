from django import forms


class sms_window(forms.Form):
    
    Message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
   