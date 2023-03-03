# Generated by Django 4.1.7 on 2023-03-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_drf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='created',
        ),
        migrations.RemoveField(
            model_name='list',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.RemoveField(
            model_name='task',
            name='updated',
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
