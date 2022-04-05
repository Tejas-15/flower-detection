from django import forms
from .models import predict

class predictForm(forms.ModelForm):
    class Meta:
        model = predict
        field = ['Flower_name','Img_pre']