# Generated by Django 2.0 on 2019-05-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='problem_answer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]