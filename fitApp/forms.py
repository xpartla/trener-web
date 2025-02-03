from django import forms
from .models import BodyPart

class BodyPartForm(forms.ModelForm):
    class Meta:
        model = BodyPart
        fields = ['name', 'description']
        exclude = ['mediaPath']

