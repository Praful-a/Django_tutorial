from django import forms
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
