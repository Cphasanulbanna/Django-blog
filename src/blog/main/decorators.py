from django.urls import reverse
import json

from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Posts


def allow_self(function):
    def wrapper(request, *args, **kwargs):
        id = kwargs["id"]
        if not Posts.objects.filter(id=id,author__user=request.user).exists():
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response_data = {
                    "status" : "err",
                    "title" : "Unauthorized access",
                    "message" : "Unauthorized access",
                }
                return HttpResponse(json.dumps(response_data),content_type="application/json")
            else:
                return HttpResponseRedirect(reverse("web:index"))
        return function(request, *args, **kwargs)
    
    return wrapper