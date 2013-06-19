from django.template import Library, Node, TemplateSyntaxError
from myproject.apps.images.models import localImage

register = Library()

def get_image_html(slug):
	im = localImage.objects.get(slug=slug)
	tag = r'<img src="%s"><div class="media caption">%s</div>'%(im.image.url, im.caption)
	return tag
	
register.simple_tag(get_image_html)


