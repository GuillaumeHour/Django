from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from photo import views


urlpatterns = patterns('',
    url(r'^image/(?P<pk>\d+)/$', views.ImageView.as_view(),name='image-view',),
    url(r'^$', views.ListImage.as_view(),name ='Photo-List',),
    url(r'^image/add/$', views.ImageCreate.as_view(), name = 'create-image',),
    url(r'update/(?P<pk>\d+)/$', views.ImageUpdate.as_view(),name='image-update',),

) 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
