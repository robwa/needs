# Generated by Django 2.2.9 on 2020-02-13 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('means', '0001_initial'),
        ('needs', '0003_auto_20200212_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='need',
            name='proposed_means',
            field=models.ManyToManyField(to='means.Means'),
        ),
    ]
