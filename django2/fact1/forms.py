from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length=10)
    input=forms.IntegerField(min_value=0,label="num")