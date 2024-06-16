# Generated by Django 5.0.4 on 2024-06-10 09:06

import ckeditor_uploader.fields
import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0004_remove_outline_stc_subject_stc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outline',
            name='image',
        ),
        migrations.AddField(
            model_name='outline',
            name='up_file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='subject',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='outline',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dvzsftuep/image/upload/v1718008117/e83yxveneoxzwh4ehfvu.png', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Lecturer'), (3, 'Student')], default=3),
        ),
    ]
