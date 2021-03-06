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
                ('Location_Amenitie_Location_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Location_Amenitie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location_Amenitie_Carparking', models.BooleanField()),
                ('Location_Amenitie_Carparking_Latitide', models.IntegerField()),
                ('Location_Amenitie_Carparking_Longitude', models.IntegerField()),
                ('Location_Amenitie_Catering_Base', models.BooleanField()),
                ('Location_Amenitie_Catering_Base_Latitude', models.IntegerField()),
                ('Location_Amenitie_Catering_Base_Longitude', models.IntegerField()),
                ('Location_Amenitie_Controlling_Status', models.CharField(max_length=100)),
                ('Location_Amenitie_Genset_Parking', models.BooleanField()),
                ('Location_Amenitie_Genset_Parking_Latitude', models.IntegerField()),
                ('Location_Amenitie_Genset_Parking_Longitude', models.IntegerField()),
                ('Location_Amenitie_Location_Id', models.IntegerField()),
                ('Location_Amenitie_Truck_Parking_Latitude', models.IntegerField()),
                ('Location_Amenitie_Truck_Parking_Longitude', models.IntegerField()),
                ('Location_Amenitie_Vanity_Parking', models.BooleanField()),
                ('Location_Amenitie_Vanity_Parking_Latitude', models.IntegerField()),
                ('Location_Amenitie_Vanity_Parking_Longitude', models.IntegerField()),
                ('Location_Amenitie_Washroom', models.BooleanField()),
                ('Location_Amenitie_Modified_Date', models.DateField(auto_now_add=True)),
                ('Location_Amenitie_Created_Date', models.DateField(auto_now_add=True)),
                ('Location_Amenitie_Creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locatonamenities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Location_Amenitie_Comment_Location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location_Amenitie.Location_Amenitie'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Location_Amenitie_Location_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentLocation_Amenitie', to=settings.AUTH_USER_MODEL),
        ),
    ]
