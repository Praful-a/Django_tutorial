from django.shortcuts import render
from .forms import AuthorF, BookF
from .models import AuthorForm, BookForm
# from .forms import ArticleFormSet

# Create your views here.


# def form(request):
#     form = ArticleFormSet
#     context = {'form': form}
#     return render(request, 'form.html', context)

def form2(request):
    form2 = AuthorF
    if request.method == 'POST':
        form2 = AuthorF(request.POST)
        if form2.is_valid():
            form2.save()

    context = {'form2': form2}
    return render(request, 'form2.html', context)


def form3(request):
    form3 = BookF
    context = {'form3': form3}
    return render(request, 'form3.html', context)


def auth(request):
    form4 = AuthorForm
    context = {'form4': form4}
    return render(request, 'form4.html', context)


def bk(request):
    form5 = BookForm
    context = {'form5': form5}
    return render(request, 'form5.html', context)
