
from django import forms
from .models import PredictImg
  
class ImageForm(forms.ModelForm):
     
    class Meta:
        model = PredictImg
        fields = ['LeafName', 'userImg']