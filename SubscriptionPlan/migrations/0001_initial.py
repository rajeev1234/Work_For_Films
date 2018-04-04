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
                ('SubscriptionPlan_Comment', models.CharField(max_length=150)),
                ('SubscriptionPlan_Comment_Created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubscriptionPlan_Amount', models.IntegerField()),
                ('SubscriptionPlan_End_Date', models.DateField()),
                ('SubscriptionPlan_FOR_FILM_COIN', models.IntegerField()),
                ('SubscriptionPlan_Location_Allowed', models.BooleanField()),
                ('SubscriptionPlan_Openings_Allowed', models.BooleanField()),
                ('SubscriptionPlan_Pitch_Allowed', models.BooleanField()),
                ('SubscriptionPlan_Pitch_Box_Capacity_Image_per_pitch', models.IntegerField()),
                ('SubscriptionPlan_Start_Date', models.DateField(auto_now_add=True)),
                ('SubscriptionPlan_Type', models.CharField(max_length=200)),
                ('SubscriptionPlan_User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_SubscriptionPlan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsSubscriptionPlan', to='SubscriptionPlan.SubscriptionPlan'),
        ),
        migrations.AddField(
            model_name='comment',
            name='SubscriptionPlan_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssSubscriptionPlan', to=settings.AUTH_USER_MODEL),
        ),
    ]
