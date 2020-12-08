# Generated by Django 3.1.4 on 2020-12-07 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YarnChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('yarn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yarn_chapter', to='main_app.yarn')),
            ],
        ),
        migrations.CreateModel(
            name='YarnPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yarn_pages', to='main_app.yarnchapter')),
            ],
        ),
    ]