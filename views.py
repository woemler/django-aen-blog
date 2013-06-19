from django.shortcuts import render_to_response
from myproject.apps.blog.models import Post
from myproject.apps.tagging.models import Tag, TaggedItem
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def home(request):
	return render_to_response('home.html')
	
def about(request):
	return render_to_response('about/about.html')
	
def meta_view(request):
	values = request.META.items()
	values.sort()
	html = []
	for k,v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
	return render_to_response('meta.html', locals())
	
def test_view(request):
	return render_to_response('test.html')

#Get list of all available tags
def tag_list_view(request):
	tag_list = Tag.objects.all()
	return render_to_response('tags/tag_list.html', {'tag_list': tag_list})

#Get list of items tagged with selected tag
def tag_detail_view(request, tag):
	tag_name = tag
	#tagged_items = TaggedItem.objects.filter(name=tag_name)
	tagged_items = Post.objects.filter(tags__contains=tag_name) #Posts only
	
	paginator = Paginator(tagged_items, 10)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	
	try:
		items = paginator.page(page)
	except (EmptyPage, InvalidPage):
		items = paginator.page(paginator.num_pages)
	
	return render_to_response('tags/tagged_item_list.html', {'tagged_items': items, 'tag_name': tag_name})
	

