from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ("post", "author")
    list_display = ('post', 'text', "author", 'published_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "likes", "tags")
    list_display = ('title', 'short_text', "author", 'published_at')

    def short_text(self, obj):
        return obj.text[:100]


admin.site.register(Tag)

