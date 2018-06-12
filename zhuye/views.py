from django.http import HttpResponse
from django.shortcuts import render

from .forms import AddForm
import os

# Create your views here.

def get_ip(request):
	#ip = request.META['REMOTE_ADDR']
	# if request.META.has_key('HTTP_X_FORWARDED_FOR'):
	if 'HTTP_X_FORWARDED_FOR' in request.META:
		ip = request.META['HTTP_X_FORWARDED_FOR']
	else:
		ip = request.META['REMOTE_ADDR']  
	return HttpResponse("Your local IP is %s" % ip)


def index(request):
	if request.method == "POST":
		form = AddForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			domain = form.cleaned_data['domain']
			ping = os.popen("ping -c 3 %s" % domain)
			result = ping.readlines()
			result = str(result[0])
			result = result.split()
			result = result[2]
			return HttpResponse(result)
	else:
		form = AddForm()
		return render(request, 'zhuye/index.html', {'form': form})
