from django.shortcuts import render
from .forms import ArticleFormSet

# Create your views here.


def form(request):
    form = ArticleFormSet
    context = {'form': form}
    return render(request, 'form.html', context)
