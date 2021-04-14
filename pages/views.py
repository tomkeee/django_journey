from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args,**kwargs):
    content={
    "my_text": "Hi There!",
    "my_name": "tomasz Scierski",
    "my_number": "My number is 7623123"}
    return render(request,"home.html",content)