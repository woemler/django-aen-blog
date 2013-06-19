from django.db import models
#from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap
from django.conf import settings
import markdown
from apps.tagging.fields import TagField
from apps.tagging.models import Tag
from south.modelsinspector import add_introspection_rules
import re
import myproject.apps.blog.customTagParser as TagParser

add_introspection_rules([], ["^apps\.tagging\.fields\.TagField"]) 

class Post(models.Model):
	title = models.CharField(max_length = 200)
	subtitle = models.CharField(max_length = 1000)
	slug = models.SlugField(
		unique_for_date = 'pub_date',
		help_text = 'Automatically built from title.'
	)
	author = models.CharField(max_length = 200) #this should ideally link to the user table
	POST_CATEGORY = (
		('misc', 'Misc.'),
		('code', 'Code'),
	)
	category = models.CharField(max_length = 10, choices = POST_CATEGORY, default = 'misc')
	MARKUP_TYPE = (
		('none', 'None'),
		#('textile', 'Textile'),
		('markdown', 'Markdown'),
	)
	markup = models.CharField(max_length = 10, choices = MARKUP_TYPE, default = 'markdown')
	body = models.TextField(blank = True)  #blank=True is the same thing as saying to both the database and Django admin that an empty field is allowed, as opposed to just null=True
	pub_date = models.DateTimeField('Date published')
	enable_comments = models.BooleanField(default = True)
	PUB_STATUS = (
		(0, 'Draft'),
		(1, 'Published'),
	)
	status = models.IntegerField(choices = PUB_STATUS, default = 0)
	tags = TagField()

	class Meta:
		ordering = ('-pub_date',)
		get_latest_by = 'pub_date'
		
	#Return the object's name in unicode	
	def __unicode__(self):
		return u'%s' %(self.title)

	#Return the permalink URL
	def get_absolute_url(self):
		return "/blog/%s/%s/" %(self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

	#overwrites the default django save function if using Markdown, but not needed otherwise
	#Right now this is defaulting to Markdown, but this can be made optional depending on the markup field.
	def save(self):
		###Replace custom escape tags
		#replace static tag with static url
		self.body = re.sub('<<<\s*static_url\s*>>>', settings.STATIC_URL, self.body, re.M)
		
		#replace image tag with image
		self.body = TagParser.subImage(self.body)
		self.body = TagParser.subThumb(self.body)
		self.body = TagParser.subPygments(self.body)
		
		if self.markup == 'markdown':
			self.body = markdown.markdown(self.body, safe_mode = False)
		super(Post, self).save()

	#When django tries to get the previous entry, it will only get published ones and not drafts
	def get_previous_published(self):
		return self.get_previous_by_pub_date(status__exact = 1)

	#When django tries to get the next entry, it will only get published ones and not drafts
	def get_next_published(self):
		return self.get_next_by_pub_date(status__exact = 1)

	#lists all of the tags for an entry
	def get_tags(self):
		#return Tag.objects.get_for_objects(self)
		return self.tags.split(' ') 
