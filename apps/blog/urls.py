from django.conf.urls.defaults import *
from teamkow.blog.views import blog_list_view, blog_detail_view
from tagging.views import tagged_object_list

#info_dict = {
#	'queryset': Entry.objects.filter(status=1),
#	'date_field': 'pub_date',
#}

urlpatterns = patterns('',
	#(r'(?P<year>d{4})/(?P<month>[a-z]{3})/(?P<day>w{1,2})/(?P<slug>[-w]+)/$', 'object_detail', dict(info_dict, slug_field='slug','blog/detail.html')),
	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', blog_detail_view),
	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', blog_list_view),
	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',blog_list_view),
	(r'^(?P<year>\d{4})/$',blog_list_view),
	(r'^$', blog_list_view),
)


