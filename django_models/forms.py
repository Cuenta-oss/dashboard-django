from dataclasses import fields
from pyexpat import model
from .models import contact, infoProducto
from django import forms

class contactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        
    
    class Meta:
        model = contact
        fields = '__all__'

class productoForm(forms.ModelForm):
    class Meta:
        model = infoProducto
        fields = '__all__'
        widgets = {
            'descripcion' : forms.Textarea(attrs={'rows':3})
        }