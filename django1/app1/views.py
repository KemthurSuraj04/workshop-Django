from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'app1/index.html',{'param1':'hello world'})

def sqfct(request):
    n=5
    fct=factorial(n)
    return render(request ,'app1/square.html',{'n':n,'sqr':n**2,'fct':fct})

def factorial(n):
    pr=1
    for i in range(2,n+1):
        pr=pr*i
    return pr

def listfactorials(request):
    n=8
    d={}
    for i in range(1,n+1):
        d[i]=factorial(i)
    
    return render(request,'app1/listfactorials.html',{'factorials':d})       

def get_possibilities(s):
    if len(s) == 1:
        return [s]
    possibilities = []
    for i in range(len(s)):
        char = s[i]
        remaining_str = s[:i] + s[i+1:]
        for p in get_possibilities(remaining_str):
            possibilities.append(char + p)
    return possibilities

def permutations(request):
    if request.method == 'POST':
        input_string = request.POST.get('input_string')
        permutations = get_possibilities(input_string)
        return render(request, 'app1/perm.html', {'permutations': permutations, 'input_string': input_string})
    return render(request, 'app1/perm.html') 
# Create your views here.
