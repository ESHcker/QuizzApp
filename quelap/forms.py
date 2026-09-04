from django import forms
from .models import Prueba

# class Example_form(forms.Form):
#     fname= forms.CharField(
#         max_length=100, 
#         required = True, 
#         label = "Your name", 
#         help_text="Your name mijo"
#     )

#     lname= forms.CharField(
#         max_length = 100, 
#         label = "Your last name"
#     )

# class Example_form_db(forms.ModelForm):
#     class Meta:
#         model = Prueba
#         fields = ['name', 'number']