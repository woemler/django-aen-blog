from django import template
from django.template import defaultfilters as df

register = template.Library()

class UltraRender(template.Node):

    def __init__(self, obj_and_field):
        self.obj = template.Variable(obj_and_field.split('.')[0])
        self.t = obj_and_field.split('.')[1]

    def render(self, context):
        obj = self.obj.resolve(context)
        t = template.Template(getattr(obj, self.t))
        rendered_field = t.render(context)
        return df.safe(df.truncatewords_html(rendered_field, 150))

def ultrarender(parser, token):
    bits = token.contents.split()
    return UltraRender(bits[1])
	
ultrarender = register.tag(ultrarender)
