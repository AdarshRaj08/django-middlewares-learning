from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
# Create your views here.

def hook(request):
    print("Hii this is inside hook view")
    return HttpResponse("this is hook view")

def excp(request):
    print("Exception occurred")
    print("I am Excp View")
    a = 10/0
    return HttpResponse("This is Exp Page")



def user_info(request):
    print("I am User info View")
    context = {'name':'Rahul'}
    return TemplateResponse(request,'hooks/user.html',context)