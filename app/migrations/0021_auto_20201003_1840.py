# Generated by Django 3.0.3 on 2020-10-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200930_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wmobject_rel_notes',
            name='app_imp',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Application Impact'),
        ),
        migrations.AlterField(
            model_name='wmobject_rel_notes',
            name='objective',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Objective'),
        ),
        migrations.AlterField(
            model_name='wmobject_rel_notes',
            name='proc_imp',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Process Impact'),
        ),
        migrations.AlterField(
            model_name='wmobject_rel_notes',
            name='resolution',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Resolution'),
        ),
    ]
