
from django.urls import path
from complaint import views

urlpatterns = [
    path("login/",views.login,name='login'),
    path("",views.home,name="home"),
    path("complaint/",views.complaint,name="complaint"),
    path("login/form/<id1>/",views.form,name="form"),
    path("admin_login/",views.admin_login,name="admin"),
    path("submit/<id1>",views.submit,name='submit'),
    path("admin_login/adminpage/<id1>/",views.submitted,name="adminsubmit"),
    path("forgotpassword/",views.forgot_password,name="forgot_password"),
    path("myaccount/<id1>/",views.myaccount,name = "myaccount"),
    path("changepassword/<id1>/",views.change_password,name = "changepassword"),
    
]