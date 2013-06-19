from django.template import Library, Node, TemplateSyntaxError
from django.db.models import get_model

register = Library()

#usage: get_latest model count as variable where filter value 
      
class LatestFilteredContentNode(Node):
	def __init__(self, model, num, varname, filter_name, filter_value):
		self.num = num
		self.varname = varname
		self.filter_name = filter_name
		self.filter_value = filter_value
		self.model = get_model(*model.split('.'))
		if self.model is None:
			raise TemplateSyntaxError("Bad model: %s"%(model))

	def render(self, context):
		kwargs = {
			'status__exact': 1,
			'%s__exact' % (self.filter_name): self.filter_value
		}
		if self.num != 'all':
			context[self.varname] = self.model._default_manager.filter(**kwargs)[:self.num]
		else:
			context[self.varname] = self.model._default_manager.filter(**kwargs)
		return ''
 	
   	
def get_latest_filtered(parser, token):
	bits = token.contents.split()
	if len(bits)  != 8:
		raise TemplateSyntaxError, "get_latest tag takes exactly 7 arguments"
	if bits[3]  != 'as':
		raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
	if bits[5] != 'where':
		raise TemplateSyntaxError, "fifth argument to get_latest tag must be 'where'"
	return LatestFilteredContentNode(bits[1], bits[2], bits[4], bits[6], bits[7])


get_latest_filtered = register.tag(get_latest_filtered)

