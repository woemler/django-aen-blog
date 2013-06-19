from django.template import Library, Node, TemplateSyntaxError
from myproject.apps.images.models import localImage

register = Library()

def get_image_url(slug):
	im = localImage.objects.get(slug=slug)
	return im.image.url

register.simple_tag(get_image_url)


