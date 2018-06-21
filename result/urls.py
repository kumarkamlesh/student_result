from django.conf.urls import url
from result import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^admin_login/$', views.admin_login_form, name='admin_login_form'),
    url(r'^user_login/$', views.user_login_form, name='user_login_form'),
    url(r'^add_student/$', views.add_student, name='add_student'),
    url(r'^add_result/$', views.add_result, name='add_result'),

    url(r'^admin_dashboard/$', views.admin_dashboard, name='admin_dashboard'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^registration_form/$', views.register_form1, name='registration_form'),

    # url(r'^user_view/$', views.user_view, name='user_view'),
    url(r'^result_table/$', views.student_table, name='student_table'),

    url(r'^success/$', views.greate, name="success"),

    url(r'^student_view/$', views.student_view, name="student_view"),
    url(r'^logout/$', auth_view.logout, name="logout"),
    url(r'^student_result/$', views.student_result, name="student_result"),
    url(r'^admin_result/$', views.admin_result, name="admin_result"),
    url(r'^read/$', views.read_more, name="read"),
    # delete item  url
    url(r'^delete_student/(?P<x>\d+)$', views.delete_student, name="delete_student"),

]
