import base64
import json
import re

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from proxylist.models import Proxy


def list_proxies(request):
    return render(request, "index.html", {"proxy_list": Proxy.objects.filter(is_active=True).order_by("location")})


def json_proxy_file(request, proxy_id):
    proxy = get_object_or_404(Proxy, id=proxy_id)
    method_password = base64.b64decode(proxy.url.split("@")[0].replace("ss://", "").encode('ascii'))
    server_and_port = proxy.url.split("@")[1]
    config = {
        "server": re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', server_and_port)[0],
        "server_port": int(re.findall(r":(\d+)", server_and_port)[0]),
        "local_port": 1080,
        "password": method_password.decode("ascii").split(":")[1],
        "method": method_password.decode("ascii").split(":")[0]
    }
    response = HttpResponse(json.dumps(config), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="config.json"'
    return response
