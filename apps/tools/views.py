from django.shortcuts import render_to_response
from teamkow.tools.models import Tool


def tools_list_view(request):
	tools_list = Tool.objects.filter(status=1)
	return render_to_response('tools/list.html', locals())

#Wolfram|Alpha API powered search tool	
def wolfram_search(request):

	tool_info = Tool.objects.get(slug = 'wolfram')

	import re
	import urllib2
	result = '' #By default, a search has not been made yet
	scripts = ''
	if 'q' in request.GET:
		q = request.GET['q']
		
		#If the input field is empty
		if not q:
			result = '<p style="color:red">Please enter a valid search term and try again.</p>'
		else:
			url = 'http://api.wolframalpha.com/v2/query?input=' + q + '&format=html&appid=GV9YRU-T7HQURJJAK'
			f = urllib2.urlopen(url)
			f = f.read()
			
			#if the search failed, return the error
			if 'success="false" error="true"' in f:
				m = re.findall('\<msg\>(.+?)\<\/msg\>', f, re.S)
				result = '<p style="color:red">' + m[0] + '</p>'
			
			#If the search was a success, return the markup
			else:
				#markup
				m = re.findall('\<markup\>\s*\<\!\[CDATA\[(.+?)\]\]\>\s*\<\/markup\>', f, re.S)
				for pod in m:
					result = result + pod + '<br /><br />'
					
				#scripts
				#m = re.findall('\<scripts\>(.+?)\<\/scripts\>', f, re.S)
				#scripts = r'</script>'
				#for scr in m:
				#	scripts = scripts + scr
				
				#remove bad links
				result = re.sub('\<ul\s*class="h"\>.+?\<\/ul\>(?!\<\/li)', '', result, re.S)
	return render_to_response('tools/wolfram/wolfram.html', {'results':result, 'scripts':scripts, 'tool_info': tool_info})
	
#HTML5 Canvas Heatmap tool
def canvas_heatmap(request):
	tool_info = Tool.objects.get(slug = 'heatmap')
	return render_to_response('tools/heatmap/heatmap.html', {'tool_info': tool_info})

def whereami(request):
	import whereAmI
	
	tool_info = Tool.objects.get(slug = 'whereami')
	result = ''
	output = ''
	error = []
	
	#test
	'''
	result = '<table>'
	for k,v in request.GET.items():
		result = result + '<tr><td>' + k + '</td><td>' + v  + '</td></tr>'
	result = result + '</table>'
	'''
	
	#Check to see if a query string was passed
	if 'mode' in request.GET:
		if request.GET['mode'] == 'Single Translation':
			if request.GET['source'] == 'Nucleotide Transcript':
				output = whereAmI.TranscriptTranslation(transcript=request.GET['refseq'], position=request.GET['position'], genome=request.GET['target_genome'], mode='nucleotide', email=request.GET['email'])
			elif request.GET['source'] == 'Amino Acid Transcript':
				output = whereAmI.TranscriptTranslation(transcript=request.GET['refseq'], position=request.GET['position'], genome=request.GET['target_genome'], mode='protein', email=request.GET['email'])
			elif request.GET['source'] == 'Genome Position':
				output = whereAmI.GenomeTranslation(query_genome=request.GET['query_genome'], chromosome=request.GET['chromosome'], position=request.GET['position'], target_genome=request.GET['target_genome'], email=request.GET['email'])
			else:
				error.append('Invalid source') 
			
		elif request.GET['mode'] == 'Batch Translation':
			result = "<div><strong>This feature has not yet been configured.</strong><div>"
		
		else:
			error.append('Invalid mode')
	
	#If there were any errors in the processing, return them
	if error != []:
		result = '<div>'
		for e in error:
			result = result + '<strong>' + e + '</strong><br>'
		result = result + '</div>'
		
	#If there were results, format them into html
	if output != '':
		result = output
		
	return render_to_response('tools/whereami/whereami.html', {'tool_info': tool_info, 'results':result})
