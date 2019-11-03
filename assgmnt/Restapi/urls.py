from django.urls import path
from . import views

urlpatterns = [
    # path('',views.fn_saveCourse),
    
    path('',views.fn_Course),
 
    path('product/',views.fn_saveCourse),
    path('show/',views.fn_showProduct)
   
]