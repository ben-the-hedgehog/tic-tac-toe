# Generated by Django 2.0.3 on 2018-03-28 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0003_game_move_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'first player to move'), ('S', 'second player to move'), ('W', 'first player wins'), ('L', 'second player wins'), ('D', 'draw')], default='F', max_length=1),
        ),
    ]
