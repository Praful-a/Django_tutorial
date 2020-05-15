from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from .models import Author
# Create your views here.


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class AuthorCreate(CreateView):
    model = Author
    fields = ['name']


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
