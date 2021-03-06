from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.core.mail import send_mail

from ansr.callback.forms import CallbackForm
from ansr import settings

from .models import SiteSettings


class AnsarView(View):
    def post(self, request, *args, **kwargs):
        print('post view')
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['form_filled'] = True
            msg = 'С сайта поступила новая заявка на обратный звонок от {} номер телефона {}'.format(form.cleaned_data['name'], form.cleaned_data['phone'])
            try:
                site_settings = SiteSettings.objects.get()
            except SiteSettings.DoesNotExist:
                site_settings = {}
            send_mail('Новая заявка с сайта', msg, settings.EMAIL_HOST_USER, (settings.EMAIL_HOST_USER, site_settings.site_email))
            return redirect(reverse('index'))
