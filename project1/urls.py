from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import reverse
from . import views
from .views import DocumentsView, DocumentUpdate


urlpatterns = [
    url(r'^$', DocumentsView.as_view(), name='project1'),
#    url(r'^(?P\d+)/update/$', DocumentUpdate.as_view(), name='update'),
    url(r'^/edit/(?P<pk>\d+)/$', DocumentUpdate.as_view(), name='document_edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)