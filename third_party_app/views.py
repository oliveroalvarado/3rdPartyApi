from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from ThirdParty_proj.settings import env
from pprint import PrettyPrinter


pp =PrettyPrinter(indent=2, depth=2)


# Create your views here.

class Noun_project(APIView):
    print(env)
    def get(self, request, name):
        key = env.get("KEY")
        secret_key = env.get("SECRET_KEY") 

        auth = OAuth1(key, secret_key)
        endpoint = f"https://api.thenounproject.com/v2/icon?query={name}&limit_to_public_domain=1"
        response = requests.get(endpoint, auth= auth)
        json_response = response.json()
        # pp.pprint(json_response.get('icons')[0].get("thumbnail_url"))
        icon_url = json_response.get('icons')[0].get("thumbnail_url")
        return Response(icon_url)
