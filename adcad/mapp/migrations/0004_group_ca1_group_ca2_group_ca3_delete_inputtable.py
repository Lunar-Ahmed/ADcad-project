# Generated by Django 5.0.9 on 2024-12-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0003_inputtable_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='ca1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='ca2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='ca3',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='InputTable',
        ),
    ]