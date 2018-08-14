from django.conf.urls import url

from ajax_upload.urls import urlpatterns

from ajax_upload.tests import views

urlpatterns += [
    url(r'^test/$', views.test_view, name='ajax-uploads-test'),
]
