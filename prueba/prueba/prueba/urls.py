from django.conf.urls import include, url
from django.contrib import admin

from principal.views import IndexView

urlpatterns = [
	url('',include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', IndexView.as_view()),
]
