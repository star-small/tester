# Generated by Django 4.1.2 on 2022-10-17 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="num_right",
        ),
    ]
