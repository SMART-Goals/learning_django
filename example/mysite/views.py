# third-party imports
from django.http import HttpRequest, HttpResponse

# standard imports
import datetime
from typing import Union


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello world")


def current_datetime(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"<html><body>It is now {datetime.datetime.now()}.</body></html>")


def hours_ahead(request, offset: Union[str, int]) -> HttpResponse:
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return HttpResponse(f"<html><body>In {offset} hour(s), it will be {dt}.</body></html>")
