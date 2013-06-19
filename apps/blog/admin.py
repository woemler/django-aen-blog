#This file determines how Django handles the blog app in the Admin interface

from django.contrib import admin
from myproject.apps.blog.models import Post

class PostAdmin(admin.ModelAdmin):

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        	'/static/javascript/tinymce_setup.js',
		]

	list_display = ('title', 'pub_date', 'enable_comments', 'status')
	search_fields = ['title', 'subtitle', 'body']
	list_filter = ('pub_date', 'enable_comments', 'status')
	prepopulated_fields = {"slug": ('title',)}  #automatically builds a slug from the title
	fieldsets = (
		(None, {'fields': (('title', 'status'), 'body', ('pub_date', 'enable_comments'), 'tags', 'slug', 'markup')}),
	)

admin.site.register(Post, PostAdmin)
