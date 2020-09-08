from django.contrib import admin

from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('view_count', )

admin.site.register(Category)


# Register your models here.
