# Generated by Django 5.0 on 2023-12-29 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freeboard_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=15)),
                ('content', models.TextField()),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('updated_date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
