# Generated by Django 5.0.6 on 2024-05-24 13:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
