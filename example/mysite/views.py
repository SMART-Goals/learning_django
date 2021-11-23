# third-party imports
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# standard imports
import datetime
from typing import Union


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello world")


def current_datetime(request: HttpRequest) -> HttpResponse:
    t = get_template("current_datetime.html")
    html = t.render({"time_now": datetime.datetime.now()})
    return HttpResponse(html)


def hours_ahead(request, offset: Union[str, int]) -> HttpResponse:
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # t = get_template("hours_ahead.html")
    # html = t.render({"offset": offset, "dt": dt})
    # return HttpResponse(html)
    return render(request, "hours_ahead.html", {"offset": offset, "dt": dt})  # shortcut removes a lot of boilerplate

