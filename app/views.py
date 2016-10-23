from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import ProductForm

from .models import Product
# Create your views here.


def hello_world(request):
	product = Product.objects.order_by('id')
	tittle = "Titulo que cambia"
	template = loader.get_template('index.html')
	#template = "index.html"
	context = {
		'product' : product,
		'tittle'  : tittle,
	}

	#return render(request, template, locals())
	return HttpResponse(template.render(context, request))

def product_detail(request, pk):
	product = get_object_or_404(Product, pk = pk)
	template = loader.get_template('producto_detail.html')
	context = {
		'product': product

	}

	return HttpResponse(template.render(context, request))

def new_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			product.save()
			return 	HttpResponseRedirect('../new')
	else:
		form = ProductForm()		

	template = loader.get_template('new_product.html')
	context = {
		'form' : form
	}

	return HttpResponse(template.render(context, request))




