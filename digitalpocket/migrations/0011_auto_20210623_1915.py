# Generated by Django 3.0.5 on 2021-06-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalpocket', '0010_auto_20210623_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subfieldview',
            name='sub_field_image',
            field=models.ImageField(default='', upload_to='fields/images/subImages'),
        ),
    ]
