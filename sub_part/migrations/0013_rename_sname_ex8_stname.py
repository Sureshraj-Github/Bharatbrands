# Generated by Django 3.2.4 on 2021-12-22 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0012_rename_hrexpen_ex8'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ex8',
            old_name='sname',
            new_name='stname',
        ),
    ]
