from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    api_request = requests.get("https://api.github.com/users?since=135")
    api = json.loads(api_request.content)
    return render(request, "home.html", {"api": api})