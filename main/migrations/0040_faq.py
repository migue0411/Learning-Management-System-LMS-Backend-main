# Generated by Django 4.1.5 on 2023-01-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_alter_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': '16. FAQ ',
            },
        ),
    ]