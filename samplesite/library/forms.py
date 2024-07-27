from django import forms
from .models import IceCream
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['flavor', 'price', 'available']



