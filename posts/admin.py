import admin_thumbnails
from django.contrib import admin
from posts.models import Post, PostImage, Comment, HashTag
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class LikeUserInline(admin.TabularInline):
    model = Post.like_users.through
    verbose_name = "좋아요 한 User"
    verbose_name_plurar = f"{verbose_name} 목록"
    extra = 1

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]
    inlines = [
        CommentInline,
        PostImageInline,
        LikeUserInline,
    ]

    formfield_overrides = {
        ManyToManyField: {"widget": CheckboxSelectMultiple},
    }

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass
