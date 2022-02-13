# Generated by Django 4.0 on 2022-02-13 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_alter_internship_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifications',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='fellowships',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='hackathons',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='scolarships',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
