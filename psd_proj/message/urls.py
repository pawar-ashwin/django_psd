from django.urls import path
from .views import homeMessageView
urlpatterns = [
path('', homeMessageView, name='home'),
]
