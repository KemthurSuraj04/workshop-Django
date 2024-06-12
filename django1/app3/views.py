from django.shortcuts import render


def listfactorials(request):
    n=8
    d={}
    for i in range(1,n+1):
        d[i]=factorial(i)
    
    return render(request,'app3/listfactorials.html',{'factorials':d}) 


def factorial(n):              #a python function
    pr=1
    for i in range(2,n+1):
        pr=pr*i
    return pr

# Create your views here.
