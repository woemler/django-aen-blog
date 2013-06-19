from django.template import Library, Node
from django.db.models import get_model

register = Library()

#usage: get_latest model count as variable where filter value 

class LatestContentNode(Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))

    def render(self, context):
    	if self.num != 'all':
        	context[self.varname] = self.model._default_manager.all().order_by('-upload_date')[:self.num]
        else:
        	context[self.varname] = self.model._default_manager.all().order_by('-upload_date')
        return ''
    	
    	"""
    	if self.num != 'all':
        	context[self.varname] = self.model._default_manager.filter(status=1)[:self.num]
        else:
        	context[self.varname] = self.model._default_manager.filter(status=1)
        return ''
        """
        

def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly 4 arguments"
    if bits[3]  != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
 
    return LatestContentNode(bits[1], bits[2], bits[4])
   	
   	
get_latest = register.tag(get_latest)
