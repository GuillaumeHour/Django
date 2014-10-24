from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from photo import views


urlpatterns = patterns('',
    url(r'$', views.ListImage.as_view(),name ='Photo-List',),
    #url(r'/add/$', views.ImageCreate.as_view(),name ='Photo-add',),
    #url(r'/(?P<pk>[0-9]+)/$', views.ImageUpdate.as_view(),name ='Photo-update',),
    #url(r'/(?P<pk>[0-9]+)/delete/$', views.ImageDelete.as_View(),name = 'Photo-delete' 
    url(r'^/image/(?P<pk>\d+)/$', views.ImageView.as_view(),name='image-view',),
    
) 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
