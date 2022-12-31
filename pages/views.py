from django.views import generic
from django.contrib.auth import get_user_model


class HomePageView(generic.TemplateView):
    template_name = 'pages/home_page.html'
