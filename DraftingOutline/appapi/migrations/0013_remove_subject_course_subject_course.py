# Generated by Django 5.0.4 on 2024-06-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0012_alter_outline_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='course',
        ),
        migrations.AddField(
            model_name='subject',
            name='course',
            field=models.ManyToManyField(to='appapi.course'),
        ),
    ]