# Generated by Django 4.1.5 on 2023-01-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_studymaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_views',
            field=models.BigIntegerField(default=0),
        ),
    ]
