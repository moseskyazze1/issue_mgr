# issues/views.py
from django.views.generic import ListView
from .models import Issue

class IssueListView(ListView):
    model = Issue
    template_name = 'issue_list.html'

