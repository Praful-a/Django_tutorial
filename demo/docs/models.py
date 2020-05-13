from django.db import models

# Create your models here.
#
# class Person(models.Model):
#     name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.name
#
#
# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')
#
#     def __str__(self):
#         return self.name
#
#
# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)


# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#
# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField()
#     number_of_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return self.headline


# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField(null=True)
#
#
# class Publisher(models.Model):
#     name = models.CharField(max_length=300)
#
#
# class Book(models.Model):
#     name = models.CharField(max_length=300)
#     pages = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     rating = models.FloatField()
#     authors = models.ManyToManyField(Author)
#     Publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
#     pubdate = models.DateField(null=True)
#
#
# class Store(models.Model):
#     name = models.CharField(max_length=300)
#     books = models.ManyToManyField(Book)

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    Publication = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline