# Generated by Django 3.2.11 on 2023-04-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20230413_1024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Desciption',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]