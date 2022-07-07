from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import LinkForm
from .models import Links
from .utils import gen_link
from django.shortcuts import render


class LinkFormView(LoginRequiredMixin, FormView):
    template_name = 'contact.html'
    form_class = LinkForm
    model = Links

    def form_valid(self, form):
        if Links.objects.filter(input_link=form.input_link).exists():
            return render('contact.html', {'input_link': form.input_link,
                                           'output_link': Links.objects.filter(input_link=form.input_link).output_link})
        else:
            link = Links(user=self.request.user, input_link=form.input_link, output_link=gen_link(form.input_link))
            link.save()
            return render('contact.html', {'input_link': form.input_link, 'output_link': gen_link(form.input_link)})


class LinksListView(LoginRequiredMixin, ListView):
    model = Links
    template_name = 'links_list.html'

    def get_queryset(self):
        return Links.objects.filter(user=self.request.user)