# Generated by Django 4.0 on 2022-01-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_remove_certifications_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='fellowships',
            name='institution',
            field=models.CharField(max_length=100, null=True),
        ),
    ]