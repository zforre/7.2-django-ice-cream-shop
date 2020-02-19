from django.views import generic
from .models import IceCream

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'ice_cream/index.html'
    model = IceCream

class DetailView(generic.DetailView):
    template_name = 'ice_cream/detail.html'
    model = IceCream
    fields = ['flavor', 'base']

class CreateView(generic.CreateView):
    template_name = 'ice_cream/create.html'
    model = IceCream
    fields = '__all__' #or ['flavor']