# Generated by Django 4.0.1 on 2022-03-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataNumbers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
