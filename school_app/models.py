from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=30)
    student_sex=models.CharField(max_length=10)
class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    teacher_name=models.CharField(max_length=30)
    teacher_sex=models.CharField(max_length=30)
class Classes(models.Model):
    classes_id=models.AutoField(primary_key=True)
    classes_name=models.CharField(max_length=10)
class Subject(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=35)
class Student_Class_Combined(models.Model):
    student_class_combined_id=models.AutoField(primary_key=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    classes=models.ForeignKey(Classes,on_delete=models.CASCADE)
class Classes_Subject_Teacher_Combined(models.Model):
    classes_subject_teacher_combined_id=models.AutoField(primary_key=True)
    classes=models.ForeignKey(Classes,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
class Users(models.Model):
    school_user_id=models.AutoField(primary_key=True)
    school_user_email=models.EmailField(unique=True)
    school_user_password=models.CharField(max_length=35)
    school_user_username=models.CharField(max_length=40)
    school_user_type=models.CharField(max_length=30)
    picture=models.ImageField(upload_to="picture_school")



