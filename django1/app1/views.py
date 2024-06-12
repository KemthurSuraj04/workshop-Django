from django.shortcuts import render
import math
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello Django !!")

def calculat(request):  #hardcoded view function n=5
    n=5
    fct=math.factorial(n)
    return render(request,'app1/index.html',{'num':n,'sqr':n*n,'fact':fct})
    

# Create your views here.
