from django import forms
from blog_app.models import blog,contects

class blog_ok(forms.ModelForm):
    class Meta:
        model = blog
        fields='__all__'

class contect_ok(forms.ModelForm):
    class Meta:
        model = contects
        fields = '__all__'
