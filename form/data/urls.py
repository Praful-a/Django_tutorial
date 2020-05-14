from django.urls import path
from . import views

urlpatterns = [
    # path('form/', views.form),
    path('', views.form2),
    path('form3/', views.form3),
    path('auth/', views.auth),
    path('bk/', views.bk)
]
