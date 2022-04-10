
from django import forms
from .models import predict

class predictForm(forms.ModelForm):
    class Meta:
        model = predict
        fields = '__all__'
        labels = {'Fr_name':'Uploader Name','Img_pre':'Prediction Image'}