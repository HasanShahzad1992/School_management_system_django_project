# Generated by Django 5.0.3 on 2024-07-20 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0009_alter_classes_subject_teacher_combined_teacher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Classes_Subject_Teacher_Combined',
        ),
    ]