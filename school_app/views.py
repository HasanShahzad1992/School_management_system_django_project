from django.shortcuts import render
from django.shortcuts import redirect
from school_app import models
# Create your views here.
def load_student_add(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_student_add.html",{"username":username})
def add_student(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        name_student=initial_request_from_front_end.POST.get("name_of_student_entered")
        sex_of_student=initial_request_from_front_end.POST.get("sex_of_student_selected")
        particular_student_object=models.Student.objects.create(student_name=name_student,student_sex=sex_of_student)
        return render(initial_request_from_front_end,"load_student_add.html",{"message":"student_successfully_added","username":username})
def view_all_students(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_student_objects=models.Student.objects.all()
        return render(initial_request_from_front_end,"view_all_students.html",{"all_student_objects":all_student_objects,"username":username})
def load_student_update(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_student_objects=models.Student.objects.all()
        return render(initial_request_from_front_end,"load_student_update.html",{"all_student_objects":all_student_objects,"username":username})
def student_update(initial_request_from_front_end,student_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_student_objects=models.Student.objects.all()
        student_object=models.Student.objects.get(student_id=student_id)
        new_student_name=initial_request_from_front_end.POST.get("student_name_updated")
        edited_sex_student=initial_request_from_front_end.POST.get("sex_of_student_updated")
        student_object.student_name=new_student_name
        student_object.student_sex=edited_sex_student
        student_object.save()
        return render(initial_request_from_front_end,"load_student_update.html",{"all_student_objects":all_student_objects,"message":"student_id_updated","username":username})
def load_student_delete(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        all_student_objects=models.Student.objects.all()
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_student_delete.html",{"all_student_objects":all_student_objects,"username":username})
def delete_student(initial_request_from_front_end,student_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        student_object=models.Student.objects.get(student_id=student_id)
        student_object.delete()
        all_student_objects=models.Student.objects.all()
        return render(initial_request_from_front_end,"load_student_delete.html",{"all_student_objects":all_student_objects,"message":"student_details deleted","username":username})
def load_teacher_add(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_teacher_add.html",{"username":username})
def add_teacher(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        new_teacher_name=initial_request_from_front_end.POST.get("teacher_name_added")
        new_teacher_sex=initial_request_from_front_end.POST.get("sex_of_teacher_selected")
        teacher_object=models.Teacher.objects.create(teacher_name=new_teacher_name,teacher_sex=new_teacher_sex)
        return render(initial_request_from_front_end,"load_teacher_add.html",{"message":"new_teacher_added","username":username})
def view_all_teachers(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_teacher_objects=models.Teacher.objects.all()
        return render(initial_request_from_front_end,"view_all_teachers.html",{"all_teacher_objects":all_teacher_objects,"username":username})
def load_teacher_update(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_teacher_objects=models.Teacher.objects.all()
        return render(initial_request_from_front_end,"load_teacher_update.html",{"all_teacher_objects":all_teacher_objects,"username":username})
def teacher_update(initial_request_from_front_end,teacher_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        teacher_object=models.Teacher.objects.get(teacher_id=teacher_id)
        updated_teacher_name=initial_request_from_front_end.POST.get("teacher_name_to_be_updated")
        updated_teacher_sex=initial_request_from_front_end.POST.get("teacher_sex_to_be_updated")
        print(updated_teacher_name,"AU")
        teacher_object.teacher_name=updated_teacher_name
        teacher_object.teacher_sex=updated_teacher_sex
        teacher_object.save()
        all_teacher_objects=models.Teacher.objects.all()
        return render(initial_request_from_front_end,"load_teacher_update.html",{"all_teacher_objects":all_teacher_objects,"message":"teacher_details_updated","username":username})
def load_teacher_delete(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_teacher_objects=models.Teacher.objects.all()
        return render(initial_request_from_front_end,"load_teacher_delete.html",{"all_teacher_objects":all_teacher_objects,"username":username})
def delete_teacher(initial_request_from_front_end,teacher_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        teacher_object=models.Teacher.objects.get(teacher_id=teacher_id)
        teacher_object.delete()
        all_teacher_objects=models.Teacher.objects.all()
        return render(initial_request_from_front_end,"load_teacher_delete.html",{"all_teacher_objects":all_teacher_objects,"message":"teacher successfully deleted","username":username})
def load_class_add(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_class_add.html",{"username":username})
def add_class(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        name_class=initial_request_from_front_end.POST.get("name_given_to_class")
        print(name_class,"NM")
        class_object=models.Classes.objects.create(classes_name=name_class)
        print(class_object,"PP")
        return render(initial_request_from_front_end,"load_class_add.html",{"message":"class_details successfully added","username":username})
def view_all_classes(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_class_objects=models.Classes.objects.all()
        return render(initial_request_from_front_end,"view_all_classes.html",{"all_class_objects":all_class_objects,"username":username})
def load_class_update(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_class_objects=models.Classes.objects.all()
        return render(initial_request_from_front_end,"load_class_update.html",{"all_class_objects":all_class_objects,"username":username})
def class_update(initial_request_from_front_end,id_class):
    username=initial_request_from_front_end.session["username"]
    class_object=models.Classes.objects.get(class_id=id_class)
    new_class_name=initial_request_from_front_end.POST.get("updated_class_name")
    class_object.class_name=new_class_name
    class_object.save()
    all_class_objects=models.Classes.objects.all()
    return render(initial_request_from_front_end,"load_class_update.html",{"all_class_objects":all_class_objects,"message":"class_details_successfully_updated","username":username})
def load_class_delete(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_class_objects=models.Classes.objects.all()
        return render(initial_request_from_front_end,"load_class_delete.html",{"all_class_objects":all_class_objects,"username":username})
def delete_class(initial_request_from_front_end,id_class):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        class_object=models.Classes.objects.get(classes_id=id_class)
        class_object.delete()
        all_class_objects=models.Classes.objects.all()
        return render(initial_request_from_front_end,"load_class_delete.html",{"all_class_objects":all_class_objects,"message":"class_details_successfully_deleted","username":username})
def load_subject_add(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_subject_add.html",{"username":username})
def add_subject(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        new_subject=initial_request_from_front_end.POST.get("subject_to_be_added")
        subject_object=models.Subject.objects.create(subject_name=new_subject)
        return render(initial_request_from_front_end,"load_subject_add.html",{"message":"new_subject_has_been_added","username":username})
def view_all_subjects(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_subject_objects=models.Subject.objects.all()
        return render(initial_request_from_front_end,"view_all_subjects.html",{"all_subject_objects":all_subject_objects,"username":username})
def load_subject_update(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_subject_objects=models.Subject.objects.all()
        return render(initial_request_from_front_end,"load_subject_update.html",{"all_subject_objects":all_subject_objects,"username":username})
def subject_update(initial_request_from_front_end,id_subject):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        subject_object=models.Subject.objects.get(subject_id=id_subject)
        new_subject=initial_request_from_front_end.POST.get("updated_subject")
        subject_object.subject_name=new_subject
        subject_object.save()
        all_subject_objects=models.Subject.objects.all()
        return render(initial_request_from_front_end,"load_subject_update.html",{"all_subject_objects":all_subject_objects,"message":"subject_name_has_been_updated","username":username})
def load_subject_delete(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_subject_objects=models.Subject.objects.all()
        return render(initial_request_from_front_end,"load_subject_delete.html",{"all_subject_objects":all_subject_objects,"username":username})
def delete_subject(initial_request_from_front_end,id_subject):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        subject_object=models.Subject.objects.get(subject_id=id_subject)
        subject_object.delete()
        all_subject_objects=models.Subject.objects.all()
        return render(initial_request_from_front_end,"load_subject_delete.html",{"all_subject_objects":all_subject_objects,"message":"subject_successfully_deleted","username":username})
def load_student_class_combined_add(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_student_objects=models.Student.objects.all()
        all_class_objects=models.Classes.objects.all()
        return render(initial_request_from_front_end,"load_student_class_combined_add.html",{"all_student_objects":all_student_objects,"all_class_objects":all_class_objects,"username":username})
def student_class_combined_add(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_student_objects=models.Student.objects.all()
        all_class_objects=models.Classes.objects.all()
        student_selected=initial_request_from_front_end.POST.get("student_selected")
        class_selected=initial_request_from_front_end.POST.get("class_selected")
        student_class_object=models.Student_Class_Combined.objects.create(student_id=student_selected,classes_id=class_selected)
        return render(initial_request_from_front_end,"load_student_class_combined_add.html",{"all_student_objects":all_student_objects,"all_class_objects":all_class_objects,"message":"successfully_added","username":username})
def view_all_student_class_combined(intial_request_from_front_end):
    if intial_request_from_front_end.method=="GET":
        username=intial_request_from_front_end.session["username"]
        all_student_class_objects=models.Student_Class_Combined.objects.all()
        return render(intial_request_from_front_end,"view_all_student_class_combined.html",{"all_student_class_objects":all_student_class_objects,"username":username})
def load_student_class_combined_update(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_student_objects=models.Student.objects.all()
        all_class_objects=models.Classes.objects.all()
        all_student_class_objects=models.Student_Class_Combined.objects.all()
        return render(initial_request_from_front_end,"load_student_class_combined_update.html",{"all_student_class_objects":all_student_class_objects,"all_student_objects":all_student_objects,"all_class_objects":all_class_objects,"username":username})
def student_class_combined_update(initial_request_from_front_end,student_class_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_student_objects=models.Student.objects.all()
        all_class_objects=models.Classes.objects.all()
        all_student_class_objects=models.Student_Class_Combined.objects.all()
        updated_student_id=initial_request_from_front_end.POST.get("student_id_to_be_updated")
        updated_class_id=initial_request_from_front_end.POST.get("class_id_to_be_updated")
        student_class_object=models.Student_Class_Combined.objects.get(student_class_combined_id=student_class_id)
        student_class_object.student_id=updated_student_id
        student_class_object.classes_id=updated_class_id
        student_class_object.save()
        return render(initial_request_from_front_end,"load_student_class_combined_update.html",{"all_student_class_objects":all_student_class_objects,"all_student_objects":all_student_objects,"all_class_objects":all_class_objects,"message":"student_class_transaction_updated","username":username})
def load_student_class_combined_delete(initial_request_from_front_end):
    username=initial_request_from_front_end.session["username"]
    all_student_class_objects=models.Student_Class_Combined.objects.all()
    return render(initial_request_from_front_end,"load_student_class_combined_delete.html",{"all_student_class_objects":all_student_class_objects,"username":username})
def student_class_combined_delete(initial_request_from_front_end,student_class_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_student_class_objects=models.Student_Class_Combined.objects.all()
        particular_student_class_object=models.Student_Class_Combined.objects.get(student_class_combined_id=student_class_id)
        particular_student_class_object.delete()
        return render(initial_request_from_front_end,"load_student_class_combined_delete.html",{"all_student_class_objects":all_student_class_objects,"message":"successsfully_deleted_student_class_combined_tranasaction","username":username})
def load_class_subject_teacher_combined_add(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_class_objects=models.Classes.objects.all()
        all_subject_objects=models.Subject.objects.all()
        all_teacher_objects=models.Teacher.objects.all()
        return render(initial_request_from_front_end,"load_class_subject_teacher_combined_add.html",{"all_class_objects":all_class_objects,"all_subject_objects":all_subject_objects,"all_teacher_objects":all_teacher_objects,"username":username})
def class_subject_teacher_combined_add(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_class_objects=models.Classes.objects.all()
        all_subject_objects=models.Subject.objects.all()
        all_teacher_objects=models.Teacher.objects.all()
        added_class_id=initial_request_from_front_end.POST.get("selected_class_id")
        added_subject_id=initial_request_from_front_end.POST.get("selected_subject_id")
        added_teacher_id=initial_request_from_front_end.POST.get("selected_teacher_id")
        print(added_teacher_id,"WW")
        particular_class_object=models.Classes_Subject_Teacher_Combined.objects.create(classes_id=added_class_id,subject_id=added_subject_id,teacher_id=added_teacher_id)
        return render(initial_request_from_front_end,"load_class_subject_teacher_combined_add.html",{"all_class_objects":all_class_objects,"all_subject_objects":all_subject_objects,"all_teacher_objects":all_teacher_objects,"message":"added_successfully","username":username})
def view_all_class_subject_teacher_combined(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_class_subject_teacher_combined_objects=models.Classes_Subject_Teacher_Combined.objects.all()
        return render(initial_request_from_front_end,"view_all_class_subject_teacher_combined.html",{"all_class_subject_teacher_combined_objects":all_class_subject_teacher_combined_objects,"username":username})
def load_class_subject_teacher_combined_update(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_class_objects=models.Classes.objects.all()
        all_subject_objects=models.Subject.objects.all()
        all_teacher_objects=models.Teacher.objects.all()
        all_class_subject_teacher_combined_objects=models.Classes_Subject_Teacher_Combined.objects.all()
        return render(initial_request_from_front_end,"load_class_subject_teacher_combined_update.html",{"all_class_objects":all_class_objects,"all_subject_objects":all_subject_objects,"all_teacher_objects":all_teacher_objects,"all_class_subject_teacher_combined_objects":all_class_subject_teacher_combined_objects,"username":username})
def class_subject_teacher_combined_update(initial_request_from_front_end,class_subject_teacher_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_class_objects=models.Classes.objects.all()
        all_subject_objects=models.Subject.objects.all()
        all_teacher_objects=models.Teacher.objects.all()
        all_class_subject_teacher_combined_objects=models.Classes_Subject_Teacher_Combined.objects.all()
        updated_class_id=initial_request_from_front_end.POST.get("selected_class_id")
        updated_subject_id=initial_request_from_front_end.POST.get("selected_subject_id")
        updated_teacher_id=initial_request_from_front_end.POST.get("selected_teacher_id")
        student_class_teacher_combined_object=models.Classes_Subject_Teacher_Combined.objects.get(classes_subject_teacher_combined_id=class_subject_teacher_id)
        student_class_teacher_combined_object.classes_id=updated_class_id
        student_class_teacher_combined_object.subject_id=updated_subject_id
        student_class_teacher_combined_object.teacher_id=updated_teacher_id
        student_class_teacher_combined_object.save()
        return render(initial_request_from_front_end,"load_class_subject_teacher_combined_update.html",{"all_class_objects":all_class_objects,"all_subject_objects":all_subject_objects,"all_teacher_objects":all_teacher_objects,"all_class_subject_teacher_combined_objects":all_class_subject_teacher_combined_objects,"message":"updated_successfully","username":username})
def load_class_subject_teacher_combined_delete(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_class_subject_teacher_combined_objects=models.Classes_Subject_Teacher_Combined.objects.all()
        return render(initial_request_from_front_end,"load_class_subject_teacher_combined_delete.html",{"all_class_subject_teacher_combined_objects":all_class_subject_teacher_combined_objects,"username":username})
def class_subject_teacher_combined_delete(initial_request_from_front_end,class_subject_teacher_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_class_subject_teacher_combined_objects=models.Classes_Subject_Teacher_Combined.objects.all()
        class_subject_combined_object=models.Classes_Subject_Teacher_Combined.objects.get(classes_subject_teacher_combined_id=class_subject_teacher_id)
        class_subject_combined_object.delete()
        return render(initial_request_from_front_end,"load_class_subject_teacher_combined_delete.html",{"all_class_subject_teacher_combined_objects":all_class_subject_teacher_combined_objects,"message":"successfully deleted transaction","username":username})
def load_user_signup(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            usertype=initial_request_from_front_end.session["usertype"]
            if usertype=="admin":
                return redirect("load_admin_home_page_school")
            else:
                return redirect("load_entry_home_page_school")
        except:
             return render(initial_request_from_front_end,"load_user_signup.html")
def user_signup(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        email=initial_request_from_front_end.POST.get("email_written_by_user")
        password=initial_request_from_front_end.POST.get("password_written_by_user")
        username=initial_request_from_front_end.POST.get("username_written_by_user")
        sign_up_object=models.Users.objects.create(school_user_email=email,school_user_password=password,school_user_username=username,school_user_type="admin",picture="True")
        return render(initial_request_from_front_end,"load_user_signup.html",{"message":"successfully_added"})
def load_user_login_school(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            usertype=initial_request_from_front_end.session["usertype"]
            if usertype=="admin":
                return redirect("load_admin_home_page_school")
            elif usertype=="entry":
                return redirect("load_entry_home_page_school")
        except:
            return render(initial_request_from_front_end,"load_user_login_school.html")
def user_login_school(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        email_typed=initial_request_from_front_end.POST.get("email_written_by_user")
        password_typed=initial_request_from_front_end.POST.get("password_written_by_user")
        print(email_typed,"email")
        print(password_typed,"password")
        try:
            particular_login_object=models.Users.objects.get(school_user_email=email_typed,school_user_password=password_typed)
            initial_request_from_front_end.session["username"]=particular_login_object.school_user_username
            initial_request_from_front_end.session["usertype"]=particular_login_object.school_user_type
            initial_request_from_front_end.session["userid"]=particular_login_object.school_user_id
            initial_request_from_front_end.session["profile_picture"]=particular_login_object.picture.url
            if initial_request_from_front_end.session["usertype"]=="admin":
                return redirect("load_admin_home_page_school")
            elif initial_request_from_front_end.session["usertype"]=="entry":
                return redirect("load_entry_home_page_school")

        except:
            return render(initial_request_from_front_end,"load_user_login_school.html",{"message":"wrong email or password"})
def load_admin_home_page_school(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            usertype=initial_request_from_front_end.session["usertype"]
            userid=initial_request_from_front_end.session["userid"]
            picture_url=initial_request_from_front_end.session["profile_picture"]
            if usertype=="admin":
                return render(initial_request_from_front_end,"load_admin_home_page_school.html",{"username":username,"userid":userid,"profile_picture":picture_url})
            else:
                return redirect("load_entry_home_page_school")
        except:
            return redirect("load_user_login_school")
def load_entry_home_page_school(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            usertype=initial_request_from_front_end.session["usertype"]
            userid=initial_request_from_front_end.session["userid"]
            picture_url=initial_request_from_front_end.session["profile_picture"]
            if usertype=="entry":
                return render(initial_request_from_front_end,"load_entry_home_page_school.html",{"username":username,"userid":userid,"profile_picture":picture_url})
            else:
                return redirect("load_admin_home_page_school")
        except:
            return redirect("load_user_login_school")
def logout_school(initial_request_from_front_end):
    initial_request_from_front_end.session.flush()
    return redirect("load_user_login_school")

def upload_school_picture(initial_request_from_front_end,school_user_id):
    if initial_request_from_front_end.method=="POST":
        picture_from_front_end=initial_request_from_front_end.FILES.get("picture_taken_by_user")
        particular_picture_object=models.Users.objects.get(school_user_id=school_user_id)
        particular_picture_object.picture=picture_from_front_end
        particular_picture_object.save()
        if initial_request_from_front_end.session["usertype"]=="admin":
            return redirect("load_admin_home_page_school")
        elif initial_request_from_front_end.session["usertype"]=="entry":
            return redirect("load_entry_home_page_school")











