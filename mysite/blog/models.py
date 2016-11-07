from django.db import models
# Register your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(
            max_length=200, default='This is a subtitle' )
    text = models.TextField()
    test_field = models.TextField(default='This is test field')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
