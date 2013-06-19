#Based on http://djangosnippets.org/snippets/2094/

from django.db import models
from django.conf import settings
from apps.tagging.fields import TagField
from apps.tagging.models import Tag
from south.modelsinspector import add_introspection_rules
import Image
import re
import os
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile

add_introspection_rules([], ["^apps\.tagging\.fields\.TagField"]) 

#Set file upload directory based on category
#http://hustoknow.blogspot.com/2010/08/try-me-out.html
def get_image_path(instance, filename):
	filename = os.path.basename(filename)
	if instance.category  == 'misc':
		return os.path.join("images", filename)
	else:
		return os.path.join("images", instance.category, filename)


class localImage(models.Model):
	title = models.CharField(max_length = 100)
	slug = models.SlugField(unique = True, help_text = 'Automatically built from title.')
	image = models.ImageField(upload_to = get_image_path)
	#image = models.ImageField(upload_to = "images")
	IMAGE_CATEGORY = (
		('family', 'Family'),
		('house', 'House'),
		('design', 'Design'),
		('misc', 'Misc.'),
	)
	category = models.CharField(max_length = 10, choices = IMAGE_CATEGORY, default = 'misc')
	#thumbnail = models.ImageField(upload_to = "images", blank = True)
	upload_date = models.DateTimeField('Date uploaded', auto_now_add=True)
	caption = models.CharField(max_length = 250, blank =True)
	tags = TagField()
    
	def __str__(self):
		return "%s"%self.title

	def __unicode__(self):
		return self.title
	"""
	def save(self, force_update=False, force_insert=False, thumb_size=(90,150)):

		image = Image.open(self.image)			
		
		if image.mode not in ('L', 'RGB'):
		    image = image.convert('RGB')
		    
		image.thumbnail(thumb_size, Image.ANTIALIAS)
		
		# save the thumbnail to memory
		temp_handle = StringIO()
		image.save(temp_handle, 'png')
		temp_handle.seek(0) # rewind the file
		
		# save to the thumbnail field
		suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
		                         temp_handle.read(),
		                         content_type='image/png')
		self.thumbnail.save(re.sub('\.\w+$', '_thumb.png', suf.name), suf, save=False)
		self.thumbnail_width, self.thumbnail_height = image.size
		
		# save the image object
		super(localImage, self).save(force_update, force_insert)
	"""	
	#lists all of the tags for an entry
	def get_tags(self):
		#return Tag.objects.get_for_objects(self)
		return self.tags.split(' ') 
