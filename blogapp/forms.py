from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
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

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Input the title.'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Blog
        fields = ['title', 'body']

        