from django.views.generic import ListView
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import IceCream
from .forms import IceCreamForm

class IceCreamCreateView(CreateView):
    model = IceCream
    form_class = IceCreamForm
    template_name = 'library/icecream_form.html'
    success_url = reverse_lazy('library:icecream-list')

    def form_valid(self, form):
        if self.check(form):
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def check(self, form):
        if form.cleaned_data['price'] > 0:
            return True
        else:
            form.add_error('price', 'Цена должна быть больше 0.')
            return False
class IceCreamListView(ListView):
    model = IceCream
    template_name = 'library/icecream_list.html'
    context_object_name = 'icecreams'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:book-list')
    def form_valid(self, form):
        if self.check(form):
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def check(self, form):
        if len(form.cleaned_data['title']) > 3:
            return True
        else:
            form.add_error('title', 'Title must be longer than 3 characters.')
            return False



class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'



