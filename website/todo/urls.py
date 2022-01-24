from django.urls import path
from . import views
urlpatterns = [
    path('', views.Homeview.as_view(), name='home'),
]