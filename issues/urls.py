# issues/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IssueListView.as_view(), name='issue_list'),
]
