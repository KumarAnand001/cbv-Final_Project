# Generated by Django 4.2 on 2024-01-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('teste', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('price', models.FloatField()),
            ],
        ),
    ]
