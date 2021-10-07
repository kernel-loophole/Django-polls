from django.contrib import admin
from django.contrib.auth.models import User
from .models import Author, Blog, Choice, Entry, Question, artist, booking, test, uploadfile, uploadimg, user

admin.site.register(Question)
admin.site.register(test)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Choice)
admin.site.register(artist)
admin.site.register(booking)
admin.site.register(uploadfile)
admin.site.register(uploadimg)
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display=('name','email','passwd')
    ordering=("name",)
    search_fields=('name','email')
     