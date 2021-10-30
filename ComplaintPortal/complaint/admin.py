from django.contrib import admin
from complaint.models import Student,Complaint,AdminLogin
# Register your models here.
admin.site.register(Student)
admin.site.register(Complaint)
admin.site.register(AdminLogin)