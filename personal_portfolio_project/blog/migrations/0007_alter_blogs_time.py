# Generated by Django 4.1.3 on 2022-11-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogs_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
