from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),   # Home Page

    # Authentication Related Patterns
    path('u/register', views.get_user_registration, name='register'),  # GET Registration
    path('u/register/create', views.save_user_registration, name='save_register'),   # POST Registration
    path('u/login', views.get_user_login, name='get_login'),  # GET Login
    path('u/login/auth', views.authenticate_login, name='auth_login'),  # POST Login data

    # Yarn Related URL Patterns
    path('yarn', views.get_yarn_form, name='get_yarn_form'),  # GET Yarn Form
    path('yarn/create', views.save_yarn, name='save_yarn'),

    # Thread Related URL Patterns
    path('thread', views.get_thread_form, name='get_thread_form'),
    path('thread/create', views.save_thread, name='save_thread'),

]
