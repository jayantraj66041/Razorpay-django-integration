from django.shortcuts import render
from django.views import View
from .models import Products
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'home.html', {
            'products': Products.objects.filter(status=True)
        })

class Details(View):
    def get(self, request, id):
        return render(request, 'detail.html', {
            'product': Products.objects.get(id=id)
        })
