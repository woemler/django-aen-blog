from django.template import Library, Node, TemplateSyntaxError
from myproject.apps.images.models import localImage
from sorl.thumbnail import get_thumbnail

register = Library()

def get_image_carousel(*args):

	tag = '<div style="height:450px; width:680px"><div id="photoCarousel" class="carousel slide">'
	
	#Add indicators
	'''
	tag = tag + '<ol class="carousel-indicators">'
		
	for j in range(len(args)):
		if j == 0:
			tag = tag + '<li data-target="#photoCarousel" data-slide-to="%d" class="active"></li>'%(j)
		else:
			tag = tag + '<li data-target="#photoCarousel" data-slide-to="%d"></li>'%(j)
		
	tag = tag + '</ol>'
	'''
		
	tag = tag + '<div class="carousel-inner">'
	
	for i in range(len(args)):

		im = localImage.objects.get(slug=args[i])

		thumb = get_thumbnail(im.image, '680x450')
		if i == 0:
			tag = tag + '<div class="active item" style="height:450px; width:680px"><a href="%s"><img src="%s" width="%s" height="%s" title="%s" ></a><div class="carousel-caption"><p>%s</p></div></div>'%(im.image.url, thumb.url, thumb.width, thumb.height, im.caption, im.caption)
		else:
			tag = tag + '<div class="item" style="height:450px; width:680px"><a href="%s"><img src="%s" width="%s" height="%s" title="%s" ></a><div class="carousel-caption"><p>%s</p></div></div>'%(im.image.url, thumb.url, thumb.width, thumb.height, im.caption, im.caption)
	
	tag = tag + '''
		</div>
		<a class="carousel-control left" href="#photoCarousel" data-slide="prev">&lsaquo;</a>
		<a class="carousel-control right" href="#photoCarousel" data-slide="next">&rsaquo;</a>
		</div>
		</div>
		<script type="text/javascript">$(document).ready(function(){$('#photoCarousel').carousel();});</script>
	'''
		
	return tag

register.simple_tag(get_image_carousel)
