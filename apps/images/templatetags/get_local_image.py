from django.template import Library, Node, TemplateSyntaxError
from myproject.apps.images.models import localImage
from sorl.thumbnail import get_thumbnail
import re

register = Library()

def get_local_image(slug, size='full'):
	
	try:
		im = localImage.objects.get(slug=slug)

		#Thumbnail with custom size
		if re.match('\d+x\d+', size):
			thumb = get_thumbnail(im.image, size)
			tag = r'<a href="%s"><img src="%s"></a><div class="media caption">%s</div>'%(im.image.url, thumb.url, im.caption)
		#Fit page width
		elif size == 'fit':
			thumb = get_thumbnail(im.image, '640x640')
			tag = r'<a href="%s"><img src="%s"></a><div class="media caption">%s</div>'%(im.image.url, thumb.url, im.caption)
		#Get full size image
		elif size == 'full':
			tag = r'<a href="%s"><img src="%s"></a><div class="media caption">%s</div>'%(im.image.url, im.image.url, im.caption)
		else:
			raise TemplateSyntaxError, "get_local_image tag arguments improperly formatted."
			
	except DoesNotExist:
		tag = '<i><b>Image not found!</b></i>'
		
	return tag

register.simple_tag(get_local_image)
