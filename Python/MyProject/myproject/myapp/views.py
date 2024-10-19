from django.shortcuts import render
from django.http import HttpResponse

def text_response_view(request):
    return HttpResponse("это текстовый ответ от сервера")

def html_response_view(request):
    return render(request, 'my_template.html')
