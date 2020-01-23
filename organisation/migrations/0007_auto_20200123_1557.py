# Generated by Django 3.0.2 on 2020-01-23 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0006_auto_20200123_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='org',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Organisation'),
        ),
    ]
