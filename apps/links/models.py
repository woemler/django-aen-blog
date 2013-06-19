from django.db import models
from apps.tagging.fields import TagField
from apps.tagging.models import Tag
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^apps\.tagging\.fields\.TagField"]) 

class Link(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    LINK_CATEGORY = (
    	('elsewhere', 'Elsewhere'),
    	('findme', 'Find Me Here'),
    )
    category = models.CharField(max_length = 10, choices = LINK_CATEGORY, default = 'elsewhere')
    url = models.CharField(max_length=400)
    date = models.DateTimeField('Date published')
    tags = TagField()
    PUB_STATUS = (
		(0, 'Draft'),
		(1, 'Published'),
	)
    status = models.IntegerField(choices = PUB_STATUS, default=1)

    class Meta:
        ordering = ('-date',)
        get_latest_by = 'date'

    def __unicode__(self):
        return u'%s' %(self.title)

    def get_absolute_url(self):
        return "/link/%s/" %(self.id)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

