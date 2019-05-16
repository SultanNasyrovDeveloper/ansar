from django.shortcuts import render, redirect, reverse
from ansr.core.views import AnsarView

from ansr.catalog.models import Product
from ansr.callback.forms import CallbackForm
from ansr.core.models import SiteSettings

from .models import IndexPageBanner, IndexPageSettings, IndexPageAdvantages, IndexPageTestimonials


class IndexView(AnsarView):
    def get(self, request, *args, **kwargs):
        context = dict()
        context['form'] = CallbackForm()
        context['banners'] = IndexPageBanner.objects.all()
        context['products'] = Product.objects.all()
        context['advantages'] = IndexPageAdvantages.objects.all()
        context['testimonials'] = IndexPageTestimonials.objects.all()
        try:
            context['site_settings'] = SiteSettings.objects.get()
        except SiteSettings.DoesNotExist:
            context['site_settings'] = {}
        try:
            context['page_settings'] = IndexPageSettings.objects.get()
        except IndexPageSettings.DoesNotExist:
            context['page_settings'] = {}
        return render(request, 'index/index.html', context)

