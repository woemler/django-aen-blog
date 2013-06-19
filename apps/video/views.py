from django.shortcuts import render_to_response
from myproject.apps.video.models import externalVideo

def get_all_videos(request):
	all_videos = externalVideo.objects.all().order_by('-upload_date')
	return render_to_response('media/videos_full.html', locals())
	
