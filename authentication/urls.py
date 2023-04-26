from django.urls import path
from .views import GroupView

urlpatterns = [
  path('group-view/', GroupView.as_view(), name='group_view')
]