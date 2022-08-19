# Generated by Django 4.0.6 on 2022-08-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='webinars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=50)),
                ('issue', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
