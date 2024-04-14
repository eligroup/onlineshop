from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/about_us.html'

# Create your views here.
