from django.forms import ModelForm, widgets
from django import forms
from . models import Blog
from ckeditor.widgets import CKEditorWidget

class CreateForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-label'}),
            'short_desc': forms.TextInput(attrs={'class':'form-label'}),
            'id': forms.TextInput(attrs={'class':'form-label'}),
            'content': forms.TextInput(attrs={'class':'form-label'}),
            'thumbnail': forms.TextInput(attrs={'class':'form-label'}),
            'name': forms.TextInput(attrs={'class':'form-label'}),
            'created_at': forms.TextInput(attrs={'class':'form-label'}),

        }