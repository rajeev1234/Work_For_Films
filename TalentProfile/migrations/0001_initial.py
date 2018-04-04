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
                ('TalentProfile_Comment', models.CharField(max_length=150)),
                ('TalentProfile_Comment_Created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TalentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_TalentProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsTalentProfile', to='TalentProfile.TalentProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='TalentProfile_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssTalentProfile', to=settings.AUTH_USER_MODEL),
        ),
    ]
