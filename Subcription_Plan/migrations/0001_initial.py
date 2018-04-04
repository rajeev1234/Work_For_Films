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
                ('subcription_plan_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='subcription_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(default=0)),
                ('End_Date', models.DateField(auto_now_add=True)),
                ('FOR_FILM_COIN', models.IntegerField(default=0)),
                ('Location_Allowed', models.IntegerField(default=0)),
                ('Openings_Allowed', models.IntegerField(default=0)),
                ('Pitch_Allowed', models.IntegerField(default=0)),
                ('Pitch_Box_Capacity_Image_per_pitch', models.IntegerField(default=0)),
                ('Start_Date', models.DateField(auto_now_add=True)),
                ('Type', models.CharField(max_length=200)),
                ('subcription_plan_Message', models.CharField(max_length=280)),
                ('Created_Date', models.DateTimeField(auto_now_add=True)),
                ('subcription_plan_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcription_plan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='subcription_plan_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subcription_Plan.subcription_plan'),
        ),
    ]