# Generated by Django 4.1.7 on 2023-06-02 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonaApps', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='old_tokens',
            field=models.TextField(blank=True),
        ),
    ]