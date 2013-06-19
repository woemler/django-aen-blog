from django.shortcuts import render_to_response
from myproject.apps.blog.models import Post
import time
from django.core.paginator import Paginator, InvalidPage, EmptyPage


#We need to import the time module to access strptime().  This lets us convert the string month representation to a datetime value

def blog_list_view(request, year=0, month='', day=0):
	#Day
	if day != 0:
		selected_posts = Post.objects.filter(status=1, pub_date__year = year, pub_date__month = time.strptime(month, "%b")[1], pub_date__day = day)
	
	#Month
	elif month != '':
		selected_posts = Post.objects.filter(status=1, pub_date__year = year, pub_date__month = time.strptime(month, "%b")[1])
	
	#Year
	elif year != 0:
		selected_posts = Post.objects.filter(status=1, pub_date__year = year)
	
	#for the latest posts
	else:
		selected_posts = Post.objects.filter(status=1)
		
	paginator = Paginator(selected_posts, 10)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	
	try:
		posts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	
	return render_to_response('blog/list.html', {"selected_posts": posts})
	
	
def blog_detail_view(request, year, month, day, slug):
	selected_post = Post.objects.get(status=1, pub_date__year = year, pub_date__month = time.strptime(month, "%b")[1], pub_date__day = day, slug = slug)
	return render_to_response('blog/detail.html', locals())
	
def code_list_view(request):
	code_list = Post.objects.filter(status=1, category='code')
	return render_to_response('code/list.html', locals())
	
def media_temp_view(request):
	return render_to_response('media/media.html', locals())
