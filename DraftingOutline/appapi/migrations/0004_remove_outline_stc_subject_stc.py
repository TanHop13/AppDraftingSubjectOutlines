# Generated by Django 5.0.4 on 2024-06-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0003_outline_stc_alter_outline_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outline',
            name='stc',
        ),
        migrations.AddField(
            model_name='subject',
            name='stc',
            field=models.IntegerField(default=3),
        ),
    ]