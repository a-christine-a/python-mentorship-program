from urllib import response
import requests
import re

def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = response.get(url)
        print(r.text)
    return r.text

def prepare_urls(matches):
    return list({match.replace("\\u0026","&") for match in matches})
url = input("Enter Instagram url : ")
response = get_response(url)

vid_matches = re.findall('"video_url":"([^"]+)"',response)
pic_matches = re.findall('"display_url":"([^"]+)"', response)

vid_urls = prepare_urls(vid_matches)
pic_urls = prepare_urls(pic_matches)

if vid_urls:
    print(f"Detected Videos : \n{vid_urls}\n")

if pic_urls:
    print(f"Detected pictures : \n{pic_urls}\n")

if not(vid_urls or pic_urls):
    print("No videos or images found")