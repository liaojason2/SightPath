# Generated by Django 4.2.1 on 2023-06-03 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_competition_topic_alter_room_name_message_room_topic"),
    ]

    operations = [
        migrations.RenameField(
            model_name="competition", old_name="Name", new_name="name",
        ),
    ]
