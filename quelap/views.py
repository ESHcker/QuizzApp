from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import Example_form, Example_form_db
# from .models import Prueba

#Create index of page
def index(request):
    return render(request, 'quelap/index.html')

#Example normal page
# def hello_with_name(request, name):
#     return render(request, 'hello_name.html', {'name' : name})

#Example form
# def example_form(request):
#     if request.method == "POST":
#         form = Example_form(request.POST)

#         if form.is_valid():
#             fname = form.cleaned_data['fname']
#             lname = form.cleaned_data['lname']
#             return HttpResponse(f"Put name: {fname} con last name: {lname}")

#     form = Example_form()
#     return render(request, 'form.html', {"form" : form})

#Example form with db
# def example_form_db(request):
#     if request.method == "POST":
#         form = Example_form_db(request.POST)
#         if form.is_valid():
#             form.save()

#     data = Prueba.objects.all()
#     form = Example_form_db()
#     return render(request, 'prueba_form_db.html', {'form' : form, 'data' : data})

