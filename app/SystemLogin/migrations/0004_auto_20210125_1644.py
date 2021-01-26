# Generated by Django 3.1.5 on 2021-01-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SystemLogin', '0003_auto_20210125_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='name',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='user_name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(max_length=255, null=True, verbose_name='fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(max_length=255, null=True, verbose_name='apodo'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male'), ('personalized', 'personalized')], max_length=255, null=True, verbose_name='sexo'),
        ),
    ]
