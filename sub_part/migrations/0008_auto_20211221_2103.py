# Generated by Django 3.2.4 on 2021-12-21 15:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0007_remove_itemexpen_tid'),
    ]

    operations = [
        migrations.CreateModel(
            name='miscexpen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('etype', models.CharField(max_length=100)),
                ('purp', models.CharField(max_length=100)),
                ('amt', models.CharField(max_length=100)),
                ('pacc', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='login',
            new_name='loginn',
        ),
        migrations.RenameModel(
            old_name='register',
            new_name='registerr',
        ),
        migrations.AddField(
            model_name='itemexpen',
            name='tid',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
