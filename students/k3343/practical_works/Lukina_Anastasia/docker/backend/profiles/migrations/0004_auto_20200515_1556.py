# Generated by Django 2.0.6 on 2020-05-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
