from django.urls import path
from .views import BookCreateView, BookListView, IceCreamCreateView, IceCreamListView

app_name = 'library'

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add/', BookCreateView.as_view(), name='book-create'),
    path('icecreams/', IceCreamListView.as_view(), name='icecream-list'),
    path('icecreams/add/', IceCreamCreateView.as_view(), name='icecream-add'),
]
