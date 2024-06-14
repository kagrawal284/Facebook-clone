from django.contrib import admin
from core.models import Post, Gallery, Friend, FriendRequest, Comment, ReplyComment, Group, Page, GroupPost, PagePost
# Register your models here.


class GalleryAdminTab(admin.TabularInline):
    model = Gallery

class PostAdmin(admin.ModelAdmin):
    inlines = [GalleryAdminTab]
    list_editable = ['active']
    list_display = ['thumbnail', 'user', 'title', 'visibility', 'active']
    prepopulated_fields = {"slug" : ("title" ,)}


class GalleryAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_display = ['thumbnail', 'post', 'active']


class FriendRequestAdmin(admin.ModelAdmin):
    list_editable = ['status']
    list_display = ['sender', 'receiver', 'status']


class FriendAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'active']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'active']


class GroupPostTabAdmin(admin.TabularInline):
    model = GroupPost


class GroupAdmin(admin.ModelAdmin):
    list_editable = ['user', 'name', 'visibility']
    list_display = ['thumbnail', 'user', 'name', 'visibility']
    prepopulated_fields = {"slug" : ("name",)}



class PageAdmin(admin.ModelAdmin):
    list_editable = ['user', 'name', 'visibility']
    list_display = ['thumbnail', 'user', 'name', 'visibility']
    prepopulated_fields = {"slug" : ("name",)}





admin.site.register(Post, PostAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplyComment, ReplyAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(GroupPost)
admin.site.register(PagePost)