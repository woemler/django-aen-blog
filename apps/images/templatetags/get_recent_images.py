from django.template import Library, Node, TemplateSyntaxError
from myproject.apps.images.models import localImage

register = Library()

#Usage: {% get_recent_images 4 category %}

def get_latest_filtered(parser, token):
	bits = token.contents.split()
	#Too many args
	if len(bits)  > 3:
		raise TemplateSyntaxError, "get_recent_images tag takes exactly 3 arguments"
	#Get all images
	elif len(bits) == 1:
		images = localImage.objects.all()
	#All images
	elif len(bits) == 2 and bits[2] == 'all':
		images = localImage.objects.all()
	#Number of images
	elif len(bits) == 2 and bits[2] != 'all':
		images = localImage.objects.all()[:bits[2]]
	#All and filter
	elif len(bits) == 3 and bits[2] == 'all':
		images = localImage.objects.filter(category=bits[3])
	#Number and filter
	elif len(bits) == 3 and bits[2] != 'all':
		images = localImage.objects.filter(category=bits[3])[:bits[2]]
	
	return images
	
get_recent_images = register.tag(get_recent_images)


