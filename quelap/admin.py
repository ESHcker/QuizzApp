from django.contrib import admin
from .models import test, question, option

@admin.register(test)
class test_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'categories')
    search_display = ('title', 'description', 'categories')
    list_filter = ('title', 'description', 'categories')

@admin.register(question)
class test_question(admin.ModelAdmin):
    list_display = ('text', 'test')
    search_display = ('text', 'test')
    list_filter = ('text', 'test')

@admin.register(option)
class test_question(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    search_display = ('text', 'question', 'is_correct')
    list_filter = ('text', 'question', 'is_correct')    