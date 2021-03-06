# Generated by Django 2.2.11 on 2021-02-10 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('year', models.TextField()),
                ('genre', models.CharField(choices=[('pop', 'pop'), ('classical', 'classical'), ('instrumental', 'instrumental')], default='pop', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('singer', models.TextField()),
                ('composer', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.Album')),
            ],
        ),
    ]
