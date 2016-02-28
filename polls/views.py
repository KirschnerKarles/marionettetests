from django.http import HttpResponse


def index(request):
	return HttpResponse("Cacat pe bat !")
