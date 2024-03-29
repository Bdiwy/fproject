# Generated by Django 4.2.3 on 2023-07-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('act', models.BooleanField(default=True)),
            ],
        ),
    ]
