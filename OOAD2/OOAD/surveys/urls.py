from django.urls import path
from . import views
from .views import deleteview
from django.contrib.auth import views as auth_views
from surveys.views import student
from django.conf.urls import include,url

#from django.contrib import admin
#from users import views as user_views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('login/', auth_views.LoginView.as_view(template_name='surveys/login.html',redirect_authenticated_user=True), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='surveys/logout.html'), name='logout-page'),
    path('staff/', views.staff, name='staff-page'), 
    path('status/', views.status, name='status-page'),
    path('dashboard/', views.staff_dashboard, name='staff_dashboard-page'),
    path('stdashboard/', views.stdashboard, name='student_dashboard-page'),
    path('student/', views.student, name='student-page'),
    path('<int:pk>/delete/', deleteview.as_view(),name='form-delete'),
    #path('delete/', views.delete_new, name='form-delete'),	
    #url(r'^admin/', admin.site.urls),

]