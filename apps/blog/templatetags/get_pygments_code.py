from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


def get_pygments_code(parser, token):
    bits = token.contents.split()
    if len(bits) > 2:
        raise TemplateSyntaxError, "get_pygments_code tag takes exactly one argument"
    
	return highlight(bits[1], PythonLexer(), HtmlFormatter())

get_pygments_code = register.tag(get_pygments_code)


   	
