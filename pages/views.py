from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "accounts/profile.html"



# Create your views here.
