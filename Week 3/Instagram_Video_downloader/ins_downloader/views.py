from urllib3 import response
import requests
import re
from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        url = request.POST['url']
        response = get_response(url)
        vid_matches = re.findall('"video_url":"([^"]+)"',response)
        pic_matches = re.findall('"display_url":"([^"]+)"', response)
        vid_urls = prepare_urls(vid_matches)
        pic_urls = prepare_urls(pic_matches)
        messages.success(request, f"Provided URL is {url}")
        print(url)
        context={
           'vid_url' : vid_urls,
           'pic_url' : pic_urls,
           'no_vid': len(vid_urls),
           'no_pic': len(pic_urls),
        }
        return render(request, "result.html",context)
    return render(request, "index.html")

def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = response.get(url)
        print(r.text)
    return r.text

def prepare_urls(matches):
    return list({match.replace("\\u0026","&") for match in matches})


