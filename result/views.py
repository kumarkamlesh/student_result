from django.shortcuts import render, redirect
from .models import registration_form1
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import add_stu, final_result, contact
from django.utils import timezone
from .models import admin_view
from django.contrib import messages


# from passlib.hash import pbkdf2_sha256


# Create your views here.

# def home(request):
#     return HttpResponse("hello this is the first django program")


def home(request):
    return render(request, 'result/home.html')


def add_result(request):
    return render(request, 'result/add_result.html')


def login(request):
    return render(request, 'result/login.html')


# contact us function
def contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact_num = request.POST['contact_num']
        messaged = request.POST['messaged']
        cont_obj = contact()
        cont_obj.name = name
        cont_obj.email = email
        cont_obj.contact_num = contact_num
        cont_obj.messaged = messaged
        cont_obj.save()
    return render(request, 'result/contact_us.html')


# bout us function
def about_us(request):
    return render(request, 'result/about_us.html')


# admin login
def admin_login_form(request):
    if 'email' in request.session:
        email = request.session['email']
        return redirect('homeurl:admin_dashboard')
    elif request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if (len(admin_view.objects.filter(email=email)) and len(admin_view.objects.filter(password=password))):
            request.session['email'] = email
            return render(request, 'result/admin_dashboard.html')
    return render(request, 'result/admin_login_form.html')


def user_login_form(request):
    if 'e' in request.session:  # if session is  alredy exixt
        e = request.session['e']
        return redirect('homeurl:student_view')

    elif request.method == "POST":
        e = request.POST['email']
        p = request.POST['password']

        if (len(registration_form1.objects.filter(email=e)) and len(registration_form1.objects.filter(password=p))):
            request.session['e'] = e  # for create session
            return redirect('homeurl:student_view')
    return render(request, 'result/user_login_form.html')


# registration form
def register_form1(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        # enc_pass = pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
        dob = request.POST['dob']
        mobile = request.POST['mobile']
        address = request.POST['address']
        regis_form = registration_form1()
        regis_form.username = username
        regis_form.firstname = firstname
        regis_form.lastname = lastname
        regis_form.email = email
        regis_form.password = password
        regis_form.conf_password = conf_password
        regis_form.dob = dob
        regis_form.mobile = mobile
        regis_form.address = address
        if (registration_form1.objects.filter(email=email).exists()):
            messages.warning(request, 'username or email alredy exist')
            return render(request, 'result/registration_form.html')
        else:
            regis_form.save()

            return redirect('homeurl:user_login_form')
    return render(request, 'result/registration_form.html')


def student_detail(request):
    return render(request, 'result/student_detail.html')


def admin_dashboard(request):
    return render(request, 'result/admin_dashboard.html')


def student_view(request):
    print(2)
    if request.method == "POST":
        print(1)
        serach = request.POST['serach']
        sem = request.POST['subcategory1']
        obj = final_result.objects.filter(roll_no=serach).filter(semester=sem)
        print(obj)
        return render(request, 'result/result_table.html', {'data': obj})

    return render(request, 'result/student_view.html')


# first sem result table


# return render(request,'result/admin_dashboard.html')


# def user_view(request):
#     return render(request, 'result/user_view.html')


def add_student(request):
    if request.method == "POST":
        roll = request.POST['roll']
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        course = request.POST['course']
        branch = request.POST['branch']
        sem = request.POST['sem']

        email = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        mobile = request.POST['mobile']
        address = request.POST['address']
        stu_add = add_stu()
        stu_add.roll = roll
        stu_add.username = username
        stu_add.firstname = firstname
        stu_add.lastname = lastname
        stu_add.course = course
        stu_add.branch = branch
        stu_add.sem = sem

        stu_add.email = email
        stu_add.password = password

        stu_add.dob = dob
        stu_add.mobile = mobile
        stu_add.address = address
        stu_add.save()

        return redirect('homeurl:success')
    return render(request, 'result/add_student.html')


def greate(request):
    return render(request, 'result/success.html')


# add student result function and class

def student_result(request):
    if request.method == "POST":

        roll_no = request.POST['roll_no']
        student_name = request.POST['student_name']
        course = request.POST['course']
        branch = request.POST['branch']
        semester = request.POST['semester']
        sub1 = request.POST['sub1']
        sub2 = request.POST['sub2']
        sub3 = request.POST['sub3']
        sub4 = request.POST['sub4']
        sub5 = request.POST['sub5']
        sub6 = request.POST['sub6']
        sub7 = request.POST['sub7']
        sub8 = request.POST['sub8']
        sub9 = request.POST['sub9']
        marks = request.POST['marks']
        marks2 = request.POST['marks2']
        marks3 = request.POST['marks3']
        marks4 = request.POST['marks4']
        marks5 = request.POST['marks5']
        marks6 = request.POST['marks6']
        marks7 = request.POST['marks7']
        marks8 = request.POST['marks8']
        marks9 = request.POST['marks9']
        seminar = request.POST['seminar']
        total = request.POST['total']
        percentage = request.POST['percentage']

        final_result_obj = final_result()
        final_result_obj.roll_no = roll_no
        final_result_obj.student_name = student_name
        final_result_obj.course = course
        final_result_obj.branch = branch
        final_result_obj.semester = semester
        # final_result_obj.semester = semester
        final_result_obj.sub1 = sub1
        final_result_obj.sub2 = sub2
        final_result_obj.sub3 = sub3
        final_result_obj.sub4 = sub4
        final_result_obj.sub5 = sub5
        final_result_obj.sub6 = sub6
        final_result_obj.sub7 = sub7
        final_result_obj.sub8 = sub8
        final_result_obj.sub9 = sub9
        final_result_obj.marks = marks
        final_result_obj.marks2 = marks2
        final_result_obj.marks3 = marks3
        final_result_obj.marks4 = marks4
        final_result_obj.marks5 = marks5
        final_result_obj.marks6 = marks6
        final_result_obj.marks7 = marks7
        final_result_obj.marks8 = marks8
        final_result_obj.marks9 = marks9
        final_result_obj.seminar = seminar
        final_result_obj.total = total
        final_result_obj.percentage = percentage
        if (final_result.objects.filter(roll_no=roll_no).exists()) and (
                final_result.objects.filter(semester=semester).exists()):

            messages.warning(request, 'Roll no and semester already exists')
            return render(request, 'result/add_student_result.html')

        # elif (final_result.objects.filter(roll_no=roll_no).exists()) and (
        #         final_result.objects.filter(student_name=student_name).exists()):
        #     messages.warning(request, 'Roll no and semester already exists')
        #     return render(request, 'result/add_student_result.html')

        else:

            final_result_obj.save()

        messages.success(request, "Saved Successfully")
        return redirect('homeurl:student_result')

    return render(request, 'result/add_student_result.html')


def student_table(request):
    return render(request, 'result/result_table.html')


# admin result view function
def admin_result(request):
    data = final_result.objects.all()
    return render(request, 'result/admin_result_view.html', {'data': data})


def delete_student(request, x):
    # date_time = final_result.objects.all()
    # print(date_time)
    a = final_result.objects.filter(id=x)
    a.delete()
    return redirect('homeurl:admin_result')


def read_more(request):
    return render(request, 'result/read_more1.html')
