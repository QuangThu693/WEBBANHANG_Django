# Generated by Django 4.2.7 on 2023-11-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_slider_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='link',
            field=models.URLField(default=''),
        ),
    ]
