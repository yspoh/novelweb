# Generated by Django 2.2 on 2020-10-09 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='title',
            fields=[
                ('book_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100)),
                ('status', models.CharField(default=False, max_length=10)),
                ('author', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=20)),
                ('info', models.CharField(max_length=300)),
                ('last_update', models.DateTimeField(null=True)),
                ('last_list_id', models.IntegerField(null=True)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NovelWeb.title')),
            ],
        ),
        migrations.CreateModel(
            name='list',
            fields=[
                ('list_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NovelWeb.title')),
            ],
        ),
    ]