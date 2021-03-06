# Generated by Django 3.0.3 on 2020-10-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_wmobject_object_sprint'),
    ]

    operations = [
        migrations.CreateModel(
            name='field_map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_class', models.CharField(max_length=200)),
                ('app_field', models.CharField(max_length=200)),
                ('map_field', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('A', 'ACTIVE'), ('I', 'INACTIVE')], default='INACTIVE', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='wmobject',
            name='object_sprint',
        ),
        migrations.AddField(
            model_name='wmobject',
            name='object_type',
            field=models.CharField(default='Other', max_length=200),
        ),
    ]
