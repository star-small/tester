# Generated by Django 4.1.2 on 2022-10-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0002_remove_question_num_right"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.CharField(max_length=250, unique=True, verbose_name="Текст"),
        ),
    ]
