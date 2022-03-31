from django.contrib import admin
from posts.models import *

# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_author', 'post_date']


admin.site.register(Posts, PostsAdmin)


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(Authors, AuthorsAdmin)


class CommentsAdmin(admin.ModelAdmin):
    # Deshabilito añadir comentarios desde el admin site de Django, ya que solo deberían añadirse desde los posts.
    def has_add_permission(self, request):
        return False


admin.site.register(Comments, CommentsAdmin)
