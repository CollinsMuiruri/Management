# Generated by Django 3.1.3 on 2020-11-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20201113_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=10)),
            ],
        ),
    ]
