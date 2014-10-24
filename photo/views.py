from django.views.generic import ListView, DetailView, UpdateView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from photo.models import Album, Image
from django.conf import settings

class ListImage(ListView):
    context_object_name = 'object_list'
    template_name = 'image_list.html'
    model = Image
    def get_queryset(self):
        return Image.objects.all()
    
    
    
class ImageView(DetailView):
    model = Image
    template_name = 'image.html'
    
class ImageCreate(CreateView):
    model = Image
    #template_name='photo/image_create.html'
    
class ImageUpdate(UpdateView):
    model = Image
    #template_name = 'photo/image_update.html'
    
class ImageDelete(DeleteView):
    model = Image
    #template_name = 'photo/image_delete.html'
    success_url = reverse_lazy('Photo-List')