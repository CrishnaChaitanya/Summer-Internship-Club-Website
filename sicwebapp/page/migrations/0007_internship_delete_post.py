# Generated by Django 4.0 on 2022-01-21 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_scolarships_referral_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('event_host', models.CharField(blank=True, max_length=150)),
                ('role', models.CharField(max_length=50)),
                ('format', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('registration_open', models.DateField()),
                ('registration_close', models.DateField()),
                ('eligibility', models.TextField()),
                ('referral_link', models.CharField(max_length=100)),
                ('branch', models.CharField(choices=[('Engineering', 'Engineering'), ('Management', 'Management'), ('Medical and Para-medical', 'Medical and Para-medical'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Law', 'Law'), ('Sciences', 'Sciences')], default='Everyone', max_length=50)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
