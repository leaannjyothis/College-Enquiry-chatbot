from django.urls import path
from .import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('register1/',views.register1,name="register1"),
    path('login1/',LoginView.as_view(template_name='login1.html'),name='login1'),
    #path('login1/',views.login1,name='login1'),
    path('afterlogin',views.afterlogin_view,name='afterlogin'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_request,name='logout'),
    path('student_signup/',views.student_signup,name='student_signup'),
    
    path('studentbot/',views.studentbot,name='studentbot'),
    
    path('course/',views.course,name='course'),
    path('admin_login/',views.admin_login,name='adminlogin'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
     path('userlist/',views.user_list,name='user_list'),
    path('delete_user/<int:uid>/',views.delete_user,name='delete_user'),
    path('edit_user/<int:uid>/',views.edit_user,name='edit_user'),
    path('timetable/',views.timtable,name='timetable'),
    path('fees/',views.fees,name='fees'),  
    path('chatmate/', views.chatmate, name='chatmate'),
    
    path('teachbot/',views.teachbot,name='teachbot'),
    
    path('tregister/', views.tregister, name='tregister'),
    path('login/', views.login_view, name='login'),
    path('tprofile/', views.tprofile, name='tprofile'),
    path('thome/', views.thome, name='thome'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout1/', views.logout_view, name='logout1'),
    
    path('add_event/', views.add_event, name='add_event'),
    path('view_events/', views.view_events, name='view_events'),
    path("books/", views.book_list, name="book_list"),
    path('cgpa/', views.cgpa, name='cgpa'),
    
]
