from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'add.html')

def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res1=x+y
    x=int(request.GET['num3'])
    y=int(request.GET['num4'])
    res2=x-y
    x=int(request.GET['num5'])
    y=int(request.GET['num6'])
    res3=x*y
    x=int(request.GET['num7'])
    y=int(request.GET['num8'])
    res4=x/y
    return render(request,'result.html',{'result1':res1,'result2':res2,'result3':res3,'result4':res4})

def result(request):
    return render(request,'result.html')