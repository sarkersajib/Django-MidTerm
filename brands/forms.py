from django import forms 
from .models import Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        #fields = ['name','bio']