from django.contrib import admin
from .models import CareerCategory, Answer, Question, Survey, User
# Register your models here.

admin.site.register(User)
admin.site.register(CareerCategory)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Survey)