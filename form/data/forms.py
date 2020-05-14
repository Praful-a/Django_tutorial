from django import forms
from .models import Author, Book
from django.forms import modelform_factory
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

#
# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(
#         max_length=3,
#         widget=forms.Select(choices=TITLE_CHOICES),
#     )
#     birth_date = forms.DateField(required=False)
#


# class AuthorF(ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'title', 'birth_date')
#         widgets = {
#             'name': Textarea(attrs={'cols': 80, 'rows': 20}),
#         }

class AuthorF(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            }
        }


class BookF(forms.Form):
    class Meta:
        model = Book
        fields = ['name', 'authors']
        Form = modelform_factory(Book, form=BookF,
                                 widget={'title': Textarea()})


'''
import datetime
from django.forms import formset_factory
from django.forms import BaseFormSet


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


ArticleFormSet = formset_factory(ArticleForm, extra=2)
formset = ArticleFormSet(initial=[
    {'title': 'Django is now open source',
     'pub_date': datetime.date.today(), }
])


class BaseArticleFormSet(BaseFormSet):
    def clean(self):
        """Checks that no two articles have the same title."""
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid no.
            return titles = []

        for form in self.forms():
            if self.can_delete and self._should_delete_form(form):
                continue
            title = form.cleaned_data.get('title')
            if title in titles:
                raise forms.ValidationError("Articles in a set must have distinct titles.")
            titles.append(title)
        ordering_widget = HiddenInput

        def get_ordering_widget(self):
            return HiddenInput(attrs={'class': 'ordering'})


ArticleFormSet = formset_factory(ArticleForm, formset=BaseArticleFormSet, can_order=True)
'''
