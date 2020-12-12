from django.urls import path
from main_app.views import UserRegistration
from . import views

urlpatterns = [
    path('', views.index, name='home'),   # Home Page

    # Authentication Related Patterns
    path('u/auth/register', UserRegistration.as_view(), name='user_registration'),  # GET Registration
    path('u/login', views.get_user_login, name='get_login'),  # GET Login
    path('u/login/auth', views.authenticate_login, name='auth_login'),  # POST Login data

    # Yarn Related URL Patterns
    path('yarn', views.get_yarn_form, name='get_yarn_form'),  # GET Yarn Form
    path('yarn/create', views.save_yarn, name='save_yarn'),

    # Thread Related URL Patterns
    path('thread', views.get_thread_form, name='get_thread_form'),
    path('thread/create', views.save_thread, name='save_thread'),

]
