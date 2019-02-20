from django import forms
from .models import Account

class AccountLogIn(forms.ModelForm):
    # forms.ModelForm은 save()함수 있음
    # forms.Form은 save()함수 없음

    # email = forms.EmailField()
    # files = forms.FileField()
    # url = forms.URLField()
    # words = forms.CharField(max_length=200)
    # max_number = forms.ChoiceField(choices=[('1','one'), ('2','two'), ('3','three')])

    # post = forms.CharField(widget=forms.TextInput(
    #     attrs = {
    #         'class': 'form-control',
    #     }
    # ))

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Input your name.'}))
    pw1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    pw2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = Account
        fields = ['username', 'pw1', 'pw2']

        