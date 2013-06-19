from django.shortcuts import render_to_response
from myproject.apps.links.models import Link

def links_list_view(request):
	elsewhere_links = Link.objects.filter(status=1, category='elsewhere').order_by('date')
	findme_links = Link.objects.filter(status=1, category='findme').order_by('date')
	return render_to_response('links/list.html', {'elsewhere_links': elsewhere_links, 'findme_links': findme_links})
	

