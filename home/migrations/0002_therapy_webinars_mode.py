# Generated by Django 4.0.6 on 2022-08-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='therapy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=50)),
                ('issue', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='webinars',
            name='mode',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
