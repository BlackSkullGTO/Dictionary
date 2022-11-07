from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'translate', 'user', 'lastsuccessdate', 'countsuccess', 'countfailure', 'active')
    ordering = ('user', 'word')
    search_fields = ('user__username', 'word')
    list_filter = ('active',)
    readonly_fields = ('lastsuccessdate', 'countsuccess', 'countfailure')
    fieldsets = (
        (None, {
            'fields': ('word', 'translate', 'user', 'active')
        }),
    )

admin.site.register(Word, WordAdmin)