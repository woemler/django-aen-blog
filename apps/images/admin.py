#This file determines how Django handles the blog app in the Admin interface

from django.contrib import admin
from myproject.apps.images.models import localImage
from sorl.thumbnail import default
#from django.utils.safestring import mark_safe
ADMIN_THUMBS_SIZE = '60x60'

#Everything beyond here is optional for customizing layout
#  You could simply write 'pass' and use the default layout

class ImageAdmin(admin.ModelAdmin):
	list_display = ('my_image_thumb', 'title', 'upload_date', 'category', 'slug')
	
	def my_image_thumb(self, obj):
		if obj.image:
			thumb = default.backend.get_thumbnail(obj.image.file, ADMIN_THUMBS_SIZE)
			return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
		else:
			return "No Image" 
	my_image_thumb.short_description = 'Thumbnail'
	my_image_thumb.allow_tags = True
	
	search_fields = ['title', 'slug']
	list_filter = ('upload_date', 'category')
	prepopulated_fields = {"slug": ('title',)}  #automatically builds a slug from the title
	'''
	fieldsets = (
		(None, {'fields': (('title', 'status'), 'body', ('pub_date', 'enable_comments'), 'tags', 'slug', 'markup')}),
	)
	'''
admin.site.register(localImage, ImageAdmin)



"""
from myapp import models
from sorl.thumbnail import default
ADMIN_THUMBS_SIZE = '60x60'

class MyModelAdmin(admin.ModelAdmin):
    model = models.MyModel
    list_display = ['my_image_thumb', 'my_other_field1', 'my_other_field2', ]

    def my_image_thumb(self, obj):
        if obj.image:
            thumb = default.backend.get_thumbnail(obj.image.file, ADMIN_THUMBS_SIZE)
            return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
        else:
            return "No Image" 
    my_image_thumb.short_description = 'My Thumbnail'
    my_image_thumb.allow_tags = True
"""