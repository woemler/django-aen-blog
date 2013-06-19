from django.template import Library, Node, TemplateSyntaxError
from myproject.apps.video.models import externalVideo
import re

register = Library()

def get_external_video(slug, size='full'):
	
	try:
		vid = externalVideo.objects.get(slug=slug)
		html = vid.embed_html
		
	return html

register.simple_tag(get_external_video)
