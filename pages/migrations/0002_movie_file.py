# Generated by Django 4.0.5 on 2022-06-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='file',
            field=models.FileField(default=1, upload_to='videos/'),
            preserve_default=False,
        ),
    ]