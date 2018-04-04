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
                ('Location_Authority_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LocationAuthority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location_Authority_Detail', models.CharField(max_length=100)),
                ('Location_Authority_Email', models.EmailField(max_length=254)),
                ('Location_Authority_Google_Address', models.EmailField(default=0, max_length=254)),
                ('Location_Authority_Latitude', models.IntegerField()),
                ('Location_Authority_Longitude', models.IntegerField()),
                ('Location_Authority_Name', models.CharField(max_length=100)),
                ('Location_Authority_Postal_Address', models.CharField(max_length=100)),
                ('Location_Authority_Contact_Number', models.IntegerField()),
                ('Location_Authority_Contact_Name', models.CharField(max_length=100)),
                ('Location_Authority_Locality_City_State', models.CharField(max_length=100)),
                ('Location_Authority_Location_ID', models.IntegerField()),
                ('Location_Authority_Office_Charges', models.IntegerField()),
                ('Location_Authority_Street_Address', models.CharField(max_length=100)),
                ('Location_Authority_Modified_Date', models.DateField(auto_now_add=True)),
                ('Location_Authority_Created_Date', models.DateField(auto_now_add=True)),
                ('Location_Authority_Creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locationauthorities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Location_Authority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location_Authorities.LocationAuthority'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Location_Authority_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentLocation_Authorities', to=settings.AUTH_USER_MODEL),
        ),
    ]