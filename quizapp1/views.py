from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404, render

def index(request):
   return  render(request, 'quizapp/index1.html')