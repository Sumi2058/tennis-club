from products.models import ProductForm,Product
from django.shortcuts import render, get_object_or_404, redirect

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            form.save()### It save the data into database
            return redirect('product_list')
  
    return render(request, 'product_create.html')

def product_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'product_list.html', {'products': products})