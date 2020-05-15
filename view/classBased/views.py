from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Publisher, Book


# Create your views here.


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publishers'


class PublisherDetail(DetailView):
    # model = Publisher
    #
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()


class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'


class PublisherBookList(ListView):
    template_name = 'classBased/books_by_publisher.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)
