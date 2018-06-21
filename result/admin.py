from django.contrib import admin
from .models import registration_form1

admin.site.register(registration_form1)
# admin.site.register(user_login)
from .models import add_stu, admin_view, final_result, contact

admin.site.register(add_stu)

admin.site.register(admin_view)
admin.site.register(final_result)
admin.site.register(contact)

# Register your models here.
