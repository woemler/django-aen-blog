from django.shortcuts import render_to_response
from myproject.apps.images.models import localImage
from myproject.apps.video.models import externalVideo

def get_all_images(request):
	all_images = localImage.objects.all()
	
	#return render_to_response('media/gallery.html', {"all_images", all_images})
	return render_to_response('media/gallery.html', locals())
	
def get_media_thumbs(request):
	recent_gallery = localImage.objects.all().order_by('-upload_date')
	recent_videos = externalVideo.objects.all().order_by('-upload_date')
	return render_to_response('media/media.html', locals())

def get_gallery_thumbs(request):
	recent_misc = localImage.objects.filter(category='misc').order_by('-upload_date')
	recent_house = localImage.objects.filter(category='house').order_by('-upload_date')
	recent_family = localImage.objects.filter(category='family').order_by('-upload_date')
	recent_design = localImage.objects.filter(category='design').order_by('-upload_date')
	return render_to_response('media/gallery_list.html', locals())
	
def get_gallery_thumbs_all(request, gallery):
	gallery_thumbs = localImage.objects.filter(category=gallery).order_by('-upload_date')
	return render_to_response('media/gallery_full.html', locals())
