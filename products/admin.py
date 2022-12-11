from django.contrib import admin

from .models import Product, Comment, Grouping


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'text', 'star', 'active', ]
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_created', )
    ordering = ('-datetime_modified', )

    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'active')
    ordering = ('-datetime_create', )


admin.site.register(Grouping)
