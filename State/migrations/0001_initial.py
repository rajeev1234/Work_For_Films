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
                ('State_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('States', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsState', to='State.State'),
        ),
        migrations.AddField(
            model_name='comment',
            name='State_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssState', to=settings.AUTH_USER_MODEL),
        ),
    ]
