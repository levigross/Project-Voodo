from django.contrib import admin

from portfolio.models import Project, UserContent


class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('created_by', 'title', 'public_id')
    list_fliter = ('created_by',)
    list_diplay_links = ('public_id')
    search_fields = ['title', 'tag']
admin.site.register(Project, ProjectAdmin)