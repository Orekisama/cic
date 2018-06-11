from django.shortcuts import render, HttpResponse

# Create your views here.

def get_ip(request):
	#ip = request.META['REMOTE_ADDR']
	# if request.META.has_key('HTTP_X_FORWARDED_FOR'):
	if 'HTTP_X_FORWARDED_FOR' in request.META:
		ip = request.META['HTTP_X_FORWARDED_FOR']
	else:
		ip = request.META['REMOTE_ADDR']  
	return HttpResponse("Your local IP is: %s" % ip)
