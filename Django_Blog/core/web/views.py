from django.http import HttpResponse
from django.shortcuts import render
import redis
def Hello(request):
    r = redis.Redis(host='redis_service', port=6379, db=0)
    name = r.get("Name").decode()
    Fame = r.get("Fame").decode()
    return HttpResponse(f"Hello {name} your  {Fame}")