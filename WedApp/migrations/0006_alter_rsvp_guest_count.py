# Generated by Django 5.1.6 on 2025-02-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WedApp', '0005_media_logo_media_slide1_media_slide2_media_slide3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='guest_count',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
    ]
