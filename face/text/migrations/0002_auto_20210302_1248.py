# Generated by Django 2.2.10 on 2021-03-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetotext',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
