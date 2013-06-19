#This file determines how Django handles the blog app in the Admin interface

from django.contrib import admin
from myproject.apps.video.models import externalVideo

class externalVideoAdmin(admin.ModelAdmin):

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        	'/static/javascript/tinymce_setup.js',
		]

	list_display = ('title', 'upload_date', 'slug')
	search_fields = ['title']
	list_filter = ('upload_date',)
	prepopulated_fields = {"slug": ('title',)}  #automatically builds a slug from the title
	fieldsets = (
		(None, {'fields': ('title', 'slug', 'url', 'embed_html', 'caption', 'tags',)}),
	)

admin.site.register(externalVideo, externalVideoAdmin)
