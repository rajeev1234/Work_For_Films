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
                ('FilmProjectForPermit_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FilmProjectForPermit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FilmProjectForPermit_Category', models.CharField(max_length=100)),
                ('FilmProjectForPermit_Crew_Size', models.CharField(max_length=100)),
                ('FilmProjectForPermit_Project_Name', models.CharField(max_length=100)),
                ('FilmProjectForPermit_ScriptasFile', models.FileField(upload_to='')),
                ('FilmProjectForPermit_Synopsis', models.CharField(max_length=100)),
                ('FilmProjectForPermit_Title', models.CharField(max_length=100)),
                ('FilmProjectForPermit_Modified_Date', models.DateField(auto_now_add=True)),
                ('FilmProjectForPermit_Created_Date', models.DateField(auto_now_add=True)),
                ('FilmProjectForPermit_Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filmprojectforpermits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_FilmProjectForPermit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsFilmProjectForPermit', to='FilmProjectForPermit.FilmProjectForPermit'),
        ),
        migrations.AddField(
            model_name='comment',
            name='FilmProjectForPermit_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssFilmProjectForPermit', to=settings.AUTH_USER_MODEL),
        ),
    ]
