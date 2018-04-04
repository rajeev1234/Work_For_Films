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
                ('Help_Category_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Help_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help_Category_Name', models.CharField(max_length=100)),
                ('Help_Category_Header_Id', models.IntegerField()),
                ('Help_Category_Modified_Date', models.DateField(auto_now_add=True)),
                ('Help_Category_Created_Date', models.DateField(auto_now_add=True)),
                ('Help_Category_Creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helpcategorys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Help_Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_category.Help_Category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Help_Category_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='help_category_Comment_Author', to=settings.AUTH_USER_MODEL),
        ),
    ]
