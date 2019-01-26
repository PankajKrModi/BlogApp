from django.contrib import admin
from .models import Post, Subscribe
from .forms import SubscribeForm

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','status','created')
    list_filter = ('status','created','publish','author')
    search_fields = ('author__username', 'author__first_name', 'title')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    form = SubscribeForm

admin.site.register(Subscribe, SubscribeAdmin)
