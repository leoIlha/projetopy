from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'core/base.html'

class BurroPageView(TemplateView):
    template_name = 'core/burro.html'