# Generated by Django 5.0.3 on 2024-07-20 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0007_classes_subject_combined_teacher'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Classes_Subject_Combined',
            new_name='Classes_Subject_Teacher_Combined',
        ),
    ]