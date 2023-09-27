from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on',)
    list_filter = ('status',)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category)

