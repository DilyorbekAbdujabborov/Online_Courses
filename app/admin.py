from django.contrib import admin

from .models import User, Courses, Lessons, Videos, Coments, Likes


if not admin.site.is_registered(User):
    @admin.register(User)
    class UserAdmin(admin.ModelAdmin):
        list_display = ['pk', 'username', 'email']
        list_display_links = ['pk', 'username']
        list_editable = ['email']

@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'name', 'price']
    list_display_links = ['pk', 'name']  # `pk` list_display da bor
    list_editable = ['price']  # `pk` list_editable da emas

@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'course', 'name', 'description']
    list_display_links = ['pk', 'course']
    list_editable = ['description']

@admin.register(Videos)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'lesson', 'videos', 'created']
    list_display_links = ['pk', 'lesson']
    list_editable = ['videos']

@admin.register(Coments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'videos', 'user', 'text']
    list_display_links = ['pk', 'videos']
    list_editable = ['text']

@admin.register(Likes)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'video', 'like_or_dislike', 'author']  # `created_by` olib tashlandi
    list_display_links = ['pk', 'author']