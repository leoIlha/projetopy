from django.views.generic import TemplateView

class LoginPageView(TemplateView):
    template_name = 'core/base.html'
class HomePageView(TemplateView):
    template_name = 'core/home.html'
