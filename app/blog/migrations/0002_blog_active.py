# Generated by Django 4.2.2 on 2023-07-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]