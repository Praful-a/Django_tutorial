from django.urls import path
from .views import PublisherList, PublisherBookList


urlpatterns = [
    path('publishers/', PublisherList.as_view()),
    path('books/<publisher>/', PublisherBookList.as_view()),
]
