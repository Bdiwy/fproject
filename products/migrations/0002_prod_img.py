# Generated by Django 4.2.3 on 2023-07-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='img',
            field=models.ImageField(default='', upload_to='photo/%y/%m/%d'),
            preserve_default=False,
        ),
    ]
