from django.http import HttpResponseRedirect


def index(request):
    return HttpResponseRedirect('/rest_server/')