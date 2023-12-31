# Generated by Django 4.2.7 on 2023-11-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_slider_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.URLField(default='')),
                ('link', models.URLField(default='')),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
