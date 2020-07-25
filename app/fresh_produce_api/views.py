from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import viewsets
from fresh_produce_api.models import Product
from fresh_produce_api.serializers import ProductSerializer
from .forms import QuoteForm


# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    """Handle creating and getting of products"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/products.html'
    total_cost = 0
    products = serializer_class(queryset, many=True)
    
    def list(self, request):
        """Retrieve all products"""
        form = QuoteForm()
        return Response({'products':self.products.data, 'total_cost':self.total_cost, 'form':form}, status=200)

    def create(self, request):
        """Handles quotations"""
        if request.method == 'POST':
            form = QuoteForm(request.POST)
            if form.is_valid():
                request_product = form.cleaned_data['product']
                price = request_product[0].price
                quantity = form.cleaned_data['quantity']
                total_cost = quantity * price
        else:
            form = QuoteForm()

        return Response({'form': form, 'total_cost':total_cost, 'products':self.products.data})
