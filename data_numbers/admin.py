from django.contrib import admin

from data_numbers.models import Category, Comment, Post, Telephone, VoteCategory

admin.site.register(Telephone)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(VoteCategory)
