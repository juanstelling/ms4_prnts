from django import forms 
from .models import Subscribe


class EmailSubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email', )