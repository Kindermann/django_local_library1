# Generated by Django 2.1.7 on 2019-03-09 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='nationality',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
