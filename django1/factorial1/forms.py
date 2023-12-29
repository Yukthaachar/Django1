from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length=20)
    input=forms.IntegerField(min_value=1,max_value=10,label="num1")
