from django.contrib import admin
from .models import Tweet,comment,Profile
# Register your models here.
admin.site.register(Tweet)


@admin.register(comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('id','tweet','user','tweet_comment','created_at')
    search_fields=('user__username','tweet_comment')
    list_filter=('created_at','user')


admin.site.register(Profile)
