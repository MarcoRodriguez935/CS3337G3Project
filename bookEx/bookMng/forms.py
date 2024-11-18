from django import forms
from django.forms import ModelForm
from .models import Book

from django import forms
from .models import Comment


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book name'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter website URL'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

# Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']



