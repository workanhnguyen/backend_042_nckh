from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


class CareerCategory(models.Model):
    category_name = models.TextField(null=False, blank=False)
    explained_content = models.TextField(null=False, blank=False)
    career_content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='images/%Y/%m', null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.category_name


class Question(models.Model):
    question_content = models.TextField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id)


class Answer(models.Model):
    answer_content = models.TextField(null=False, blank=False)
    career_category = models.ForeignKey(CareerCategory, related_name='answers', on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.answer_content
