# Generated by Django 4.1.4 on 2022-12-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_momber_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='MSG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]