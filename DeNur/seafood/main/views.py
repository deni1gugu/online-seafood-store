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
from django.shortcuts import render, redirect
from django.contrib import messages
print('Файл views.py запущен')
from .forms import SeafoodForm 

def add_seafood(request):
    if request.method == 'POST':
        form = SeafoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Морепродукт успешно добавлен!')
            return redirect('seafood_list')  # Замените 'seafood_list' на имя вашего представления для списка товаров
    else:
        form = SeafoodForm()
    context = {'form': form}
    return render(request, 'main/add_seafood.html', context) 