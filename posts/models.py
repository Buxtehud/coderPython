from django.db import models


class Posts(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=40, unique=True)
    post_author = models.ForeignKey('Authors', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class Authors(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)


class Comments(models.Model):
    comment_post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    comment_date = models.DateTimeField(auto_now_add=True)
