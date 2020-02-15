# Generated by Django 2.2.9 on 2020-02-15 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20200215_1351'),
        ('needs', '0007_remove_need_proposed_patterns'),
    ]

    operations = [
        migrations.AddField(
            model_name='need',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='required_needs', to='activities.Activity'),
        ),
    ]
