from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
#from tagging.views import tagged_object_list
from socket import gethostname

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    #(r'^meta/', 'myproject.views.meta_view'),
	#(r'^test/', 'myproject.views.test_view'),
	#(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root', settings.STATIC_ROOT}),

	
	#Blog
	(r'^$', 'myproject.apps.blog.views.blog_list_view'),
	(r'^blog/$', 'myproject.apps.blog.views.blog_list_view'),
	#(r'^blog/', include('myproject.apps.blog.urls')),
	#(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', blog_detail_view),
	(r'^blog/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'myproject.apps.blog.views.blog_detail_view'),
	(r'^blog/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'myproject.apps.blog.views.blog_list_view'),
	(r'^blog/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'myproject.apps.blog.views.blog_list_view'),
	(r'^blog/(?P<year>\d{4})/$','myproject.apps.blog.views.blog_list_view'),
	
	#Media
	(r'^media/$', 'myproject.apps.images.views.get_media_thumbs'),
	(r'^media/gallery/$', 'myproject.apps.images.views.get_gallery_thumbs'),
	(r'^media/gallery/(?P<gallery>\w+)/$', 'myproject.apps.images.views.get_gallery_thumbs_all'),
	(r'^media/videos/$', 'myproject.apps.video.views.get_all_videos'),
	
	#Code
	(r'^code/$', 'myproject.apps.blog.views.code_list_view'),
	#(r'^tools/wolfram/$', 'myproject.apps.tools.views.wolfram_search'),
	#(r'^tools/heatmap/$', 'myproject.apps.tools.views.canvas_heatmap'),
	#(r'^tools/whereami/$', 'myproject.apps.tools.views.whereami'),
	
	#Links
	(r'^links/$', 'myproject.apps.links.views.links_list_view'),

	#Tags
	(r'^tags/$', 'myproject.views.tag_list_view'),
	(r'^tags/(?P<tag>[-\w]+)$', 'myproject.views.tag_detail_view'),
	
	#About
	(r'^about/$', 'myproject.views.about'),
	
	#Grappelli
	(r'^grappelli/', include('grappelli.urls')),
	
	#TinyMCE
	(r'^tinymce/', include('tinymce.urls')),
	
)



#You need this for linking to static files within the root directory
if settings.DEBUG:
	urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


