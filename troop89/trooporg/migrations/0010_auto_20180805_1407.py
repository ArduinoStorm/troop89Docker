# Generated by Django 2.1 on 2018-08-05 18:07

# Part 2: schema migration

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trooporg', '0009_migrate_type_to_integer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patrolmembership',
            name='type',
        ),
        migrations.RenameField(
            model_name='patrolmembership',
            old_name='type_transition',
            new_name='type',
        ),
    ]