from django.shortcuts import render
from django.contrib.auth.models import Group



# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
    

class GroupView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    user = request.user
    # groups = Group.objects.all()
    groups = user.groups.all()
    data = {
      'groups': [group.name for group in groups],
    }
    print(data)
    return Response(data)


