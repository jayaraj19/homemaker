# Generated by Django 3.0.2 on 2020-01-23 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200119_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', related_query_name='profile', to='account.Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/images/'),
        ),
    ]
