from django.db import models
from django.conf import settings
from apps.tagging.fields import TagField
from apps.tagging.models import Tag
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^apps\.tagging\.fields\.TagField"]) 

class externalVideo(models.Model):
	title = models.CharField(max_length = 100)
	slug = models.SlugField(unique = True, help_text = 'Automatically built from title.')
	url = models.URLField()
	embed_html = models.TextField()
	upload_date = models.DateTimeField('Date uploaded', auto_now_add=True)
	caption = models.CharField(max_length = 250, blank =True)
	tags = TagField()
    
	def __str__(self):
		return "%s"%self.title

	def __unicode__(self):
		return self.title

	#lists all of the tags for an entry
	def get_tags(self):
		return self.tags.split(' ') 
