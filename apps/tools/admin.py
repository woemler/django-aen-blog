#This file determines how Django handles the blog app in the Admin interface

from django.contrib import admin
from teamkow.tools.models import Tool

#Everything beyond here is optional for customizing layout
#  You could simply write 'pass' and use the default layout

class ToolAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'enable_comments', 'status')
	search_fields = ['title', 'body_markdown']
	list_filter = ('pub_date', 'enable_comments', 'status')
	prepopulated_fields = {"slug": ('title',)}  #automatically builds a slug from the title
	fieldsets = (
		(None, {'fields': (('title', 'status'), 'body_markdown', ('pub_date', 'enable_comments'), 'slug')}),
	)

admin.site.register(Tool, ToolAdmin)
