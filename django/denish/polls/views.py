from django.shortcuts import render

# Create your views here.
def index(request):
    var = {'name':'Denish','surname':'Borad'}
    return render(request,"home.html",var)

def contact(request):
    return render(request,'contact.html')

