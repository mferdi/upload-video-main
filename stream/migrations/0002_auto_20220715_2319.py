# Generated by Django 2.2 on 2022-07-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
