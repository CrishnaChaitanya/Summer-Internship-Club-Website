# Generated by Django 4.0 on 2022-01-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathons',
            name='link_to_apply',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]