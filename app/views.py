from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print("I am view")
    return HttpResponse("Hii this is home page")


def adarsh(request):
    print("I am view")
    return HttpResponse("Hii this is adarsh page")