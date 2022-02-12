from django import forms

class upload(forms.Form):
    file=forms.FileField()