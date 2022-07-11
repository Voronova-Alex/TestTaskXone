from django.urls import path
from .views import LinkFormView, LinksListView, relink

urlpatterns = [
    path('', LinkFormView.as_view(), name='home'),
    path('links/', LinksListView.as_view(), name='links'),
    path('<data>', relink, name='relink')
]
