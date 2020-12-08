from django.db import models

# Import User Manager
from main_app.managers import UserManager


# User Authentication & Creation Model
class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    profile_image = models.URLField(max_length=255, default='https://picsum.photos/id/1005/600/300')
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email


# Many-to-One Rel with Custom User
# Many Yarns can belong to a Customer User
class Yarn(models.Model):
    title = models.CharField(max_length=30)
    chapter = models.IntegerField()
    author = models.ForeignKey(CustomUser, related_name='yarn_author', on_delete=models.CASCADE)
    content = models.TextField()
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp


# Many-to-One Rel with Yarn
class YarnChapter(models.Model):
    chapter = models.IntegerField()
    yarn = models.ForeignKey(Yarn, related_name='yarn_chapter', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp


# Many-to-One Rel with Chapter
class YarnPages(models.Model):
    page = models.IntegerField()
    chapter = models.ForeignKey(YarnChapter, related_name='yarn_pages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp


# Many-to-One Rel with Yarn
# Many Threads can belong to a Yarn
class Thread(models.Model):
    title = models.CharField(max_length=30)
    original_yarn = models.ForeignKey(Yarn, related_name='original_yarn', on_delete=models.CASCADE)
    original_author = models.ForeignKey(CustomUser, related_name='original_author', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, related_name='thread_author', on_delete=models.CASCADE)
    content = models.TextField()
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp
