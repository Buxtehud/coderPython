from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from posts.models import *

posts = Posts.objects.all()
posts_contexts = []
for post in posts:
    post_context = {}
    post_context['title'] = post.title
    post_context['date'] = post.post_date
    post_context['author'] = post.post_author
    post_context['content'] = post.content
    posts_contexts.append(post_context)

def inicio(request):
    return render(request, 'posts/index.html', {'allposts': posts_contexts[::-1], 'destacado': posts_contexts[-1]})
