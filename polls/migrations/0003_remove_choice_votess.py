# Generated by Django 2.2.6 on 2019-10-13 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_votess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votess',
        ),
    ]
