from myproject.apps.images.templatetags.get_image_html import get_image_html
import re
from sorl.thumbnail import get_thumbnail
from myproject.apps.images.models import localImage
from pygments import highlight
from pygments.lexers import PythonLexer, HtmlSmartyLexer
from pygments.formatters import HtmlFormatter

#replace image tag with image
def subImage(body):
	image_tags = re.findall('<<<\s*img\s[-\w]+\s*>>>', body, re.I)
	for tag in image_tags:
		match = re.search('<<<\s*img\s([-\w]+)\s*>>>', tag, re.I)
		body = re.sub(tag, get_image_html(match.group(1)), body)
	return body

#Replace custom thumbnail tags with sorl thumbnail tags
def subThumb(body):
	thumb_tags = re.findall('<<<\s*thumb\s[-\w]+\s*>>>', body, re.I)
	for tag in thumb_tags:
		match = re.search('<<<\s*thumb\s([-\w]+)\s*>>>', tag, re.I)
		im = localImage.objects.get(slug=match.group(1))
		if im.image.height > 640 or im.image.width > 640:
			thumb = get_thumbnail(im.image, '640x640')
		else:
			thumb = im.image #don't bother resizing if the image fits
		thumb_tag = r'<a href="%s"><img src="%s"></a><div class="media caption">%s</div>'%(im.image.url, thumb.url, im.caption)
		body = re.sub(tag, thumb_tag, body)
	return body
	
#Replace custom pygment tags with formatted code
def	subPygments(body):
	return re.sub('<<<\s*pygments\s(\w+)\s*>>>(.+?)<<<\s*\/\s*pygments\s*>>>', replaceFunc, body, flags=re.S|re.M)
	
	
def replaceFunc(match):
	if match.group(1) == 'python':
		return highlight(match.group(2), PythonLexer(), HtmlFormatter())
	elif match.group(1) in ['html', 'javascript']:
		return highlight(match.group(2), HtmlSmartyLexer(), HtmlFormatter())
	else:
		raise Warning("Invalid lexer argument!")
