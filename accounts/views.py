from django.views.generic import TemplateView


class ProfilePageView(TemplateView):
    template_name = "accounts/profile.html"

# Create your views here.
