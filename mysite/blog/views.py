from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home page")

def post_list(request):
    return render(request, 'blog/post_list.html',{})