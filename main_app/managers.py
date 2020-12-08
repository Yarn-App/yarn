from django.contrib.auth.models import User
from django.db import models


# Validation Classes
def reg_validator(post_data):
    # Grab username & email from db
    check_username = User.objects.filter(username=post_data['username'])
    check_email = User.objects.filter(email=post_data['email'])

    errors = {}
    #  Add logic check here
    if len(post_data['username']) == 0:
        errors['username_req'] = "Username is required"
    if len(check_username) > 0:
        errors['username_check'] = "Username is taken"
    if len(post_data['email']) == 0:
        errors['email_req'] = "Email is required"
    if len(check_email) > 0:
        errors['email_check'] = "Email is already registered"
    if len(post_data['password']) == 0:
        errors['password_req'] = "A password is required"
    if post_data['confirm_password'] != post_data['password']:
        errors['confirm_password'] = "Passwords did not match"

    return errors


class UserManager(models.Manager):

    def login_validator(self, post_data):

        check_username = User.objects.filter(username=post_data['username'])

        errors = {}
        #  Add logic check here
        if len(post_data['username']) == 0:
            errors['username_login_req'] = "A username is required to login"
        if len(check_username) == 0:
            errors['username_not_found'] = "Username was not recognized"
        if len(post_data['password']) == 0:
            errors['username_not_found'] = "Password required"

        return errors
