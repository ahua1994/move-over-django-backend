# Generated by Django 4.2.2 on 2023-06-15 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('move', '0003_alter_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]