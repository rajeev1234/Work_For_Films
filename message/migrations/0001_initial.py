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
                ('messages_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Messages_Subject', models.CharField(max_length=900)),
                ('Messages_Message', models.CharField(max_length=280)),
                ('Messages_Created_Date', models.DateTimeField(auto_now_add=True)),
                ('Messages_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='messages_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='message.Messages'),
        ),
    ]
