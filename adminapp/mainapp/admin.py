from django.contrib import admin
from .models import CareerCategory, Answer, Question, Survey, User
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

admin.site.register(User)
admin.site.register(CareerCategory)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Survey)


class SurveyForm(forms.ModelForm):
    result = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Survey
        fields = "__all__"