import requests
import json
import urllib.parse, urllib.request, re
from googletrans import Translator
import openai
import os


def weather ():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q":"20.9985,105.848"}
    headers = {
        "X-RapidAPI-Key": "68845eb247msh6e0d303d434a120p187729jsn2900d5db104b",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(json.loads(json.dumps(response.text)))
    return data    


def dich(a):
    translator = Translator()
    result = translator.translate( a, src='en', dest='vi')
    return result.text

def search_url(a):
    query_string = urllib.parse.urlencode({'search_query': a})
    htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',htm_content.read().decode())
    url = "http://www.youtube.com/watch?v=" + search_results[0]
    return url	

def forecast():
    url = "https://foreca-weather.p.rapidapi.com/forecast/daily/101581130"
    querystring = {"alt":"0","tempunit":"C","windunit":"MS","periods":"12","dataset":"full"}
    headers = {
        "X-RapidAPI-Key": "68845eb247msh6e0d303d434a120p187729jsn2900d5db104b",
        "X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(json.loads(json.dumps(response.text)))
    return data

def search_gpt(ask):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
    teext = response['choices'][0]['text']
    return teext
