from django.contrib import admin
from .models import CareerCategory, Answer, Question
# Register your models here.

admin.site.register(CareerCategory)
admin.site.register(Answer)
admin.site.register(Question)
