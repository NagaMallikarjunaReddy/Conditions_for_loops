from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':1000,'b':150,'c':200}
    return render(request,'condition.html',d)

def loop(request):
    d={'name':'SNSR'}
    return render(request,'loop.html',d)