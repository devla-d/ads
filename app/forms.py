from django import forms
from .models import Advert



class Adsform(forms.ModelForm):
    cover_photos= forms.ImageField(label="Image 1")
    cover_photos_2 = forms.ImageField(label="Image 2")
    

    class Meta:
        model = Advert
        fields = ['title','cover_photos','cover_photos_2','condition','price','brand_name','description','phone','email','days']