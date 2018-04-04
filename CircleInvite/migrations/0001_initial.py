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
            name='CircleInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CircleInvite_Accepted', models.CharField(max_length=100, unique=True)),
                ('CircleInvite_Modified_Date', models.DateTimeField(auto_now_add=True)),
                ('CircleInvite_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CircleInvite_Comment', models.CharField(max_length=150)),
                ('CircleInvite_Comment_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circleinvite', to=settings.AUTH_USER_MODEL)),
                ('Comment_CircleInvite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circleinvite_comments', to='CircleInvite.CircleInvite')),
            ],
        ),
    ]
