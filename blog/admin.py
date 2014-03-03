from django.contrib import admin
from blog.models import BlogPost, BlogCategory, Comment, BlogTag

class CommentInlineAdmin(admin.StackedInline):
    model = Comment

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "posted", "title", "author")
    search_fields = ("title", "author__username")
    inlines = [CommentInlineAdmin]
    readonly_fields = ("author",)
    filter_horizontal = ("tag",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory)
admin.site.register(Comment)
admin.site.register(BlogTag)