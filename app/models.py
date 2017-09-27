from django.db import models


class Post(models.Model):

    title = models.TextField('タイトル')

    def __str__(self):
        return self.title
