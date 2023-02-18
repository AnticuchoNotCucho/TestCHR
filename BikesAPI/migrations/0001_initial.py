# Generated by Django 4.1.7 on 2023-02-18 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('altitude', models.FloatField()),
                ('ebikes', models.IntegerField()),
                ('has_ebikes', models.BooleanField()),
                ('last_updated', models.BigIntegerField()),
                ('normal_bikes', models.IntegerField()),
                ('payment', models.JSONField()),
                ('payment_terminal', models.BooleanField()),
                ('post_code', models.CharField(max_length=200)),
                ('renting', models.IntegerField()),
                ('returning', models.IntegerField()),
                ('slots', models.IntegerField()),
                ('uid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('empty_slots', models.IntegerField()),
                ('free_bikes', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BikesAPI.extra')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('company', models.JSONField()),
                ('gbfs_href', models.CharField(max_length=50)),
                ('href', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BikesAPI.location')),
            ],
        ),
    ]
