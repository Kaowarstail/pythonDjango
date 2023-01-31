# Generated by Django 4.1.3 on 2022-12-06 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_team_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberteam',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='members.member'),
        ),
        migrations.AlterField(
            model_name='memberteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='members.team'),
        ),
    ]
