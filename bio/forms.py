from django import forms
from .models import Contact
import json
import os




model_path1 = os.path.join(os.path.dirname(__file__), 'artifacts', 'columns.json')
with open(model_path1, 'rb') as file1:
        columns = json.load(file1)['data_columns']
        locations = columns[4:]

OPTIONS = ['options1','option2','option3']


class predict_form(forms.Form):
    Location = forms.ChoiceField(choices=[(option, option) for option in locations], widget=forms.Select(attrs={'class': 'form-control'}))
    Bedrooms = forms.ChoiceField(choices=[(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7)], widget=forms.Select(attrs={'class': 'form-control'}))
    SQFT = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    BathRoom = forms.ChoiceField(choices=[(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7)],widget=forms.Select(attrs={'class': 'form-control'}))
    

class Contact_form(forms.ModelForm):
    class Meta:
         model  = Contact
         fields = ('name','email','phone','message')
  