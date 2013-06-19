from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap
import markdown

class Tool(models.Model):
	title = models.CharField(max_length = 200)
	slug = models.SlugField(
		unique_for_date = 'pub_date',
		help_text = 'Automatically built from title.'
	)
	body_html = models.TextField(blank = True)  #blank=True is the same thing as saying to both the database and Django admin that an empty field is allowed, as opposed to just null=True
	body_markdown = models.TextField()
	pub_date = models.DateTimeField('Date published')
	enable_comments = models.BooleanField(default = True)
	PUB_STATUS = (
		(0, 'Draft'),
		(1, 'Published'),
	)
	status = models.IntegerField(choices = PUB_STATUS, default = 0)

	class Meta:
		ordering = ('-pub_date',)
		get_latest_by = 'pub_date'
		verbose_name_plural = 'tools'  #This will make python refer to multiple instances of Entry as entries and not Entrys

	#Return the object's name in unicode	
	def __unicode__(self):
		return u'%s' %(self.title)

	#Return the permalink URL
	def get_absolute_url(self):
		return "/tools/%s/" %(self.slug)

	#overwrites the default django save function if using Markdown, but not needed otherwise
	def save(self):
		self.body_html = markdown.markdown(self.body_markdown, safe_mode = False)
		super(Tool, self).save()

	#When django tries to get the previous entry, it will only get published ones and not drafts
	def get_previous_published(self):
		return self.get_previous_by_pub_date(status__exact = 1)

	#When django tries to get the next entry, it will only get published ones and not drafts
	def get_next_published(self):
		return self.get_next_by_pub_date(status__exact = 1)


