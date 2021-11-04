# Generated by Django 3.2.9 on 2021-11-02 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0009_alter_postcategory_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategory',
            name='subscribers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
