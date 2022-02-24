from django import forms
from contents.models import *
class PostContent(forms.ModelForm):
    class Meta:
        model = Maincontent
        fields = '__all__'
