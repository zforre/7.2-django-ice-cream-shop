from django.views import generic
from .models import IceCream

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'icecream/index.html'
    model = IceCream

class DetailView(generic.DetailView):
    template_name = 'icecream/detail.html'
    model = IceCream

class CreateView(generic.CreateView):
    template_name = 'icecream/create.html'
    model = IceCream
    fields = '__all__' #or ['flavor']