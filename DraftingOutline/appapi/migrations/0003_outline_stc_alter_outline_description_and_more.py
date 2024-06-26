# Generated by Django 5.0.4 on 2024-06-09 04:16

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='outline',
            name='stc',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='outline',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='outline',
            name='tag',
            field=models.ManyToManyField(to='appapi.tag'),
        ),
    ]
