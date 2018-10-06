from django.shortcuts import render
from resource.models.WDF import WDF, WAS
# Create your views here.


def get_was(request, was_id):
    was = WAS.objects.get(id=int(was_id))
