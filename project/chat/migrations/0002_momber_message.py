# Generated by Django 4.1.4 on 2022-12-08 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='momber',
            name='message',
            field=models.TextField(null=True),
        ),
    ]