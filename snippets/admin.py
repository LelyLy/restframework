from django.contrib import admin

from snippets.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['title', 'code', 'linenos']}),
        ('Style', {'fields': ['language', 'style']}),
        ('Additional fields', {'fields': ['owner', 'highlighted']}),
    ]
    list_display = ('created', 'title', 'code', 'owner')
    search_fields = ['title']


admin.site.register(Snippet, SnippetAdmin)
