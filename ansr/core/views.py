from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from ansr.callback.forms import CallbackForm


class AnsarView(View):
    def post(self, request, *args, **kwargs):
        print('post view')
        form = CallbackForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            request.session['form_filled'] = True
        return redirect(reverse('index'))
