# Generated by Django 3.0.5 on 2021-07-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalpocket', '0021_auto_20210729_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfile',
            name='category',
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='doc_image',
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='doc_title',
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='docs_id',
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='username',
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
