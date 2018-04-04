# Generated by Django 2.0.3 on 2018-04-04 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_station_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PoliceStation_Area_Police_Station', models.CharField(max_length=200)),
                ('PoliceStation_DCP', models.CharField(max_length=200)),
                ('PoliceStation_Station_Name', models.CharField(max_length=200)),
                ('PoliceStation_Created_Date', models.DateTimeField(auto_now_add=True)),
                ('PoliceStation_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='police_station', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='police_station_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police_station.PoliceStation'),
        ),
    ]