from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models
from django.forms import ModelForm
# Create your models here.

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]


class Author(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "% (model_name)s's %(field_labels)s are not unique."
            }
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']
