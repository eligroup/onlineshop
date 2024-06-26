# Generated by Django 4.2.2 on 2024-04-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
