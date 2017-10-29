from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailView

urlpatterns = {
    url(r'^bucketlist/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)