from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('created', 'status', 'updated')
    search_fields = ('title', 'author__username')
    prepopulated_fields = {'slug':('title', )}
    list_editable = ('status',)
    date_hierarchy = ('created')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'images')

admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Images, ImagesAdmin)