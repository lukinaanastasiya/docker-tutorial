# Generated by Django 2.0.6 on 2020-05-16 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_competition'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='ex3',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
