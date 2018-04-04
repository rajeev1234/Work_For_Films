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
                ('Help_Center_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HelpCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help_Center_Help_Name', models.CharField(max_length=100)),
                ('Help_Center_Help_Id', models.IntegerField()),
                ('Help_Center_Modified_Date', models.DateField(auto_now_add=True)),
                ('Help_Center_Created_Date', models.DateField(auto_now_add=True)),
                ('Help_Center_Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Help_Center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_center.HelpCenter'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Help_Center_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helpcenter_Comment_Author', to=settings.AUTH_USER_MODEL),
        ),
    ]
