# Generated by Django 4.1.5 on 2023-02-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_delete_universitie_remove_feedback_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='img',
            field=models.ImageField(null=True, upload_to='uploads/%Y/%m'),
        ),
    ]