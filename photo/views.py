from django.views.generic import ListView, DetailView, UpdateView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from photo.models import Tag, Image, Album
from django.conf import settings

    
class AlbumCreate(CreateView):
    model = Album
    fields = ['first_name','last_name','emails']
    template_name = 'Create_image.html'
    
class ImageView(DetailView):
    model = Image
    allow_empty = True
    template_name = 'image.html'
    
class ListImage(ListView):
    #context_object_name = 'object_list'
    template_name = 'image_list.html'
    model = Image
    #def get_queryset(self):
    #    return Image.objects.all()
    
class ImageCreate(CreateView):
    model = Image
    template_name='image_create.html'
    fields = ['title','image']
    #def form_valid(self, form):
    #    form.instance.created = self.request.user
    #    return super(ImageCreate, self).form_valid(form)
    #success_url=reverse('Photo-List')
    
    
class ImageUpdate(UpdateView):
    model = Image
    template_name = 'image_update.html'
    
class ImageDelete(DeleteView):
    model = Image
    template_name = 'photo/image_delete.html'
    success_url = reverse_lazy('Photo-List')
