# Generated by Django 2.1 on 2018-08-04 18:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trooporg', '0002_remove_patrol_date_retired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=32, unique=True)),
                ('start', models.DateField(default=datetime.date.today)),
                ('end', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patrolmembership',
            name='date_expired',
        ),
        migrations.RemoveField(
            model_name='patrolmembership',
            name='date_joined',
        ),
        migrations.AddField(
            model_name='patrolmembership',
            name='term',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='patrol_memberships', to='trooporg.Term'),
        ),
    ]
