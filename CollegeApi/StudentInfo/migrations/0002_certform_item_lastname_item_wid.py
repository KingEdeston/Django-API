# Generated by Django 4.0.5 on 2022-06-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wid', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='lastName',
            field=models.CharField(default='Smith', max_length=25),
        ),
        migrations.AddField(
            model_name='item',
            name='wid',
            field=models.CharField(default='000000', max_length=20),
        ),
    ]
