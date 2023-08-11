# Generated by Django 4.2.3 on 2023-08-11 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_femele_male'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_m', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='male',
            name='girl',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chat.femele'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_f', models.CharField(max_length=100, null=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.product')),
            ],
        ),
    ]
