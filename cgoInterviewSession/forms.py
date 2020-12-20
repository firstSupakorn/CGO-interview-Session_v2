from django import forms

class CreateNewList(forms.Form):
    x = forms.CharField(label="x")
    a = forms.CharField(label="a")
    print(x,a)


