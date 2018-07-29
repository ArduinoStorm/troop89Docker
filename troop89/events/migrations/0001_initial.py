# Generated by Django 2.0.7 on 2018-07-29 16:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36)),
                ('slug', models.SlugField(help_text='URL Slug that identifies this event. Changing this will invalidate existing urls pointing to this event.', unique_for_date='start')),
                ('description', models.TextField()),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=28)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventType'),
        ),
    ]