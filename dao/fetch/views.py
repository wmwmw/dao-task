import json

from django.views import View
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse, HttpRequest

from django.core.validators import URLValidator, ValidationError

from .utils import parse_url_to_bs
from .models import Task


class IndexView(TemplateView):
    template_name = "index.html"


class ParseURLAjax(View):
    def post(self, request: HttpRequest):
        url = request.POST.get("url")
        try:
            URLValidator()(url)
        except ValidationError:
            return JsonResponse({"msg": "Invalid url."}, status=400)

        bs = parse_url_to_bs(url)
        if not bs:
            return JsonResponse(
                {"msg": "Unable to fetch and parse given url."},
                status=500,
            )

        description = bs.head.find("meta", {"name": "description"})
        site_name = bs.head.find("meta", {"property": "og:site_name"})
        image = bs.head.find("meta", {"property": "og:image"})

        Task.objects.create(
            url=url,
            title=bs.head.title.text,
            description=description.get("content") if description else None,
            site_name=site_name.get("content") if site_name else None,
            image=image.get("content") if image else None,
        )

        return JsonResponse({"msg": "Done."}, status=200)


class GetData(ListView):
    model = Task
    template_name = "task_list"
