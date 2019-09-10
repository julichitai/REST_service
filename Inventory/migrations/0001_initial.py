# Generated by Django 2.2.5 on 2019-09-10 08:27

import Inventory.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemType', models.CharField(max_length=15, verbose_name=Inventory.models.ItemType)),
                ('quality', models.SmallIntegerField(default=100, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('owner', models.ForeignKey(null=True, on_delete='', to='Player.Player')),
            ],
        ),
    ]