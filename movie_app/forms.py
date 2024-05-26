from django import forms
from . models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','description','year','username','trailer','img']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['moviereview']