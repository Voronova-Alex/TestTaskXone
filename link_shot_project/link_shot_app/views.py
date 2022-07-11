from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView

from .forms import LinkForm
from .models import Links
from .utils import gen_link


def relink(request, data):
    if Links.objects.filter(output_link=request.build_absolute_uri('/') + data).exists():
        obj = Links.objects.get(output_link=request.build_absolute_uri('/') + data)
        link = obj.input_link
        return redirect(link)


class LinkFormView(CreateView):
    template_name = 'home.html'
    form_class = LinkForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        if not Links.objects.filter(input_link=instance.input_link, user=self.request.user).exists():
            instance.user = self.request.user
            instance.output_link = self.request.build_absolute_uri('/') + gen_link()
            instance.save()
        return render(self.request, 'link.html', {'link': instance.input_link,
                                       'new_link': Links.objects.get(input_link=instance.input_link, user=self.request.user).output_link})


class LinksListView(LoginRequiredMixin, ListView):
    model = Links
    template_name = 'links_list.html'

    def get_queryset(self):
        return Links.objects.filter(user=self.request.user)
