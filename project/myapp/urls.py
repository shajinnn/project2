from django.urls import path
from . import views

urlpatterns = [
    path('',views.myIndex),
    path('loginn/',views.fn_userLogin),
    path('register/',views.fn_reg),
    path('change/',views.fn_change_pass),
    path('profile/',views.fn_editprofile),
    path('addfriend/',views.fn_addpro),
    path('imgeupload/',views.fn_upload_img)
]