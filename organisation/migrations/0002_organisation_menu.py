# Generated by Django 3.0.2 on 2020-01-19 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menus', related_query_name='menu', to='organisation.Menu'),
        ),
    ]