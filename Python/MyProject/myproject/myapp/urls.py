from django.urls import path
from .views import text_response_view, html_response_view

urlpatterns = [
    path('text/', text_response_view, name='text_response'),
    path('html/', html_response_view, name='html_response'),
]
