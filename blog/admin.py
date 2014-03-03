from django.contrib import admin
from blog.models import BlogPost, Comment

class CommentInlineAdmin(admin.StackedInline):
    model = Comment

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [CommentInlineAdmin]
    readonly_fields = ("author",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(BlogPost, BlogPostAdmin)