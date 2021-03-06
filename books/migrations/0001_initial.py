# Generated by Django 4.0.4 on 2022-04-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('cover_image', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
