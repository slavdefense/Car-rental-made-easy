# Generated by Django 3.2.7 on 2022-01-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_alter_rent_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rent',
            options={'ordering': ['sdate']},
        ),
        migrations.RenameField(
            model_name='rent',
            old_name='date',
            new_name='edate',
        ),
        migrations.AddField(
            model_name='rent',
            name='sdate',
            field=models.DateField(default='2022-11-21'),
            preserve_default=False,
        ),
    ]
