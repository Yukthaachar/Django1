from django.urls import path
from factorial1.views import fact1
urlpatterns=[path("",fact1)]