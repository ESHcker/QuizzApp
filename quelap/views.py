from django.shortcuts import render, redirect

def index(request):
    return render(request, 'quelap/index.html')

def tests(request):
    return render(request, 'quelap/pool_tests.html')
