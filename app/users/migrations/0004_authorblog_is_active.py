# Generated by Django 4.2.2 on 2023-07-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_authorblog_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorblog',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]