# Generated by Django 3.2.4 on 2021-12-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0009_auto_20211222_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('atype', models.CharField(max_length=100)),
                ('bal', models.CharField(max_length=100)),
                ('cbal', models.CharField(max_length=100)),
            ],
        ),
    ]
