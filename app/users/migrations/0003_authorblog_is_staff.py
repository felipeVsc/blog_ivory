# Generated by Django 4.2.2 on 2023-07-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_authorblog_groups_authorblog_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorblog',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
