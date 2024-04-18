from django.shortcuts import render


def index(request):
    return render(request,'main/index.html')
def about(request):
    return render(request, 'main/about.html')

def raka(request):
    return render(request, 'main/contact.html')

def tovar(request):
    return render(request, 'main/tovar.html')

def korzin(request):
    return render(request, 'main/korzin.html')
