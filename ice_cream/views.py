from django.views import generic
from .models import IceCream
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'ice_cream/index.html'
    model = IceCream

    def get_queryset(self):
        if 'selection' in self.kwargs:
            return IceCream.objects.filter(available=self.kwargs['selection'].upper())
        return IceCream.objects.all()
        

class DetailView(generic.DetailView):
    template_name = 'ice_cream/detail.html'
    model = IceCream
    fields = ['flavor', 'base']

class CreateView(generic.CreateView):
    template_name = 'ice_cream/create.html'
    model = IceCream
    fields = '__all__' #or ['flavor']

class DeleteView(generic.DeleteView):
    model = IceCream
    success_url = reverse_lazy('ice_cream/index.html')
    def get_absolute_url(self):
            return reverse_lazy('ice_cream:index')

class UpdateView(generic.UpdateView):
    template_name = 'ice_cream/edit.html'
    model = IceCream
    fields = '__all__'