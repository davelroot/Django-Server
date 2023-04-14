
import json, stripe
from django.views import View
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator, EmptyPage
from markeplace.models import Product, Category, Customer, Order
from mainHome.models import Logotiposglass
# Create your views here.



################################################################################################
#                                         #
#                LOJA HOME- FRONTEND            #        LOJA HOME- FRONTEND
#                                         #
#                                         #
################################################################################################
# 
class Lojahome(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
  
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
  
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('markeplace:lojahome')
  
    def get(self, request, *args,  **kwargs):
        # print()
        #return HttpResponseRedirect(f'markeplace:{request.get_full_path()[3:]}')
        products = Product.objects.filter(active=True)	        
        if products:
            paginator = Paginator(products, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
            context = {
                'products':digital_products_data
            }        
	    
            context['categories'] = Category.objects.all()        
        return render(request, 'aquibazarapido/index.html', context )
  
    
def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'aquibazarapido/shop_catalog.html', data)

#################################################
#
#        ADIOCIONAR MARCAS E CATEGORIAS
#
#
#################################################
#
# 
#

 	
class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )        

class CheckOut(View):
	def post(self, request):
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		customer = request.session.get('customer')
		cart = request.session.get('cart')
		products = Product.get_products_by_id(list(cart.keys()))
		print(address, phone, customer, cart, products)

		for product in products:
			print(cart.get(str(product.id)))
			order = Order(customer=Customer(id=customer),
						product=product,
						price=product.price,
						address=address,
						phone=phone,
						quantity=cart.get(str(product.id)))
			order.save()
		request.session['cart'] = {}

		return redirect('cart')





class OrderView(View):

	def get(self, request):
		customer = request.session.get('customer')
		orders = Order.get_orders_by_customer(customer)
		print(orders)
		return render(request, 'orders.html', {'orders': orders})


class Login(View):
	return_url = None

	def get(self, request):
		Login.return_url = request.GET.get('return_url')
		return render(request, 'login.html')

	def post(self, request):
		email = request.POST.get('email')
		password = request.POST.get('password')
		customer = Customer.get_customer_by_email(email)
		error_message = None
		if customer:
			flag = check_password(password, customer.password)
			if flag:
				request.session['customer'] = customer.id

				if Login.return_url:
					return HttpResponseRedirect(Login.return_url)
				else:
					Login.return_url = None
					return redirect('homepage')
			else:
				error_message = 'Invalid !!'
		else:
			error_message = 'Invalid !!'

		print(email, password)
		return render(request, 'login.html', {'error': error_message})


def logout(request):
	request.session.clear()
	return redirect('login')

class Signup (View):
	def get(self, request):
		return render(request, 'signup.html')

	def post(self, request):
		postData = request.POST
		first_name = postData.get('firstname')
		last_name = postData.get('lastname')
		phone = postData.get('phone')
		email = postData.get('email')
		password = postData.get('password')
		# validation
		value = {
			'first_name': first_name,
			'last_name': last_name,
			'phone': phone,
			'email': email
		}
		error_message = None

		customer = Customer(first_name=first_name,
							last_name=last_name,
							phone=phone,
							email=email,
							password=password)
		error_message = self.validateCustomer(customer)

		if not error_message:
			print(first_name, last_name, phone, email, password)
			customer.password = make_password(customer.password)
			customer.register()
			return redirect('homepage')
		else:
			data = {
				'error': error_message,
				'values': value
			}
			return render(request, 'signup.html', data)

	def validateCustomer(self, customer):
		error_message = None
		if (not customer.first_name):
			error_message = "Please Enter your First Name !!"
		elif len(customer.first_name) < 3:
			error_message = 'First Name must be 3 char long or more'
		elif not customer.last_name:
			error_message = 'Please Enter your Last Name'
		elif len(customer.last_name) < 3:
			error_message = 'Last Name must be 3 char long or more'
		elif not customer.phone:
			error_message = 'Enter your Phone Number'
		elif len(customer.phone) < 10:
			error_message = 'Phone Number must be 10 char Long'
		elif len(customer.password) < 5:
			error_message = 'Password must be 5 char long'
		elif len(customer.email) < 5:
			error_message = 'Email must be 5 char long'
		elif customer.isExists():
			error_message = 'Email Address Already Registered..'
		# saving

		return error_message



#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['logotipos'] = Logotiposglass.objects.all()
#        context['brands'] = Brand.objects.all()
#        context['categories'] = Category.objects.all()
#        context['product'] = Addproduct.objects.all()
       
#        return context

################################################################################################
#                                         #
#        FILTRO PARA TODOS SEGMENTO DA LOJA            #FILTRO PARA TODOS SEGMENTO DA LOJA
#                                         #
#                                         #
################################################################################################
#




class TodosProdutos(View):

#    template_name = 'aquibazarapido/shop_single.html'

    def product_detail(request, slug=None):
            
        product = get_object_or_404(Product, slug=slug)

        

        return render(request, 'aquibazarapido/shop_single.html', {
            'product': product,
        
            })

from django.db import models
from django.conf  import settings
#from django.contrib.auth import get_user_model
# Create your models here.
import os, json, datetime
 
User = settings.AUTH_USER_MODEL


def marketplace_director_path(instance, filename):
    banner_pic_name = 'markepace/products/{0}/{1}'.format(instance.product_name, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return banner_pic_name

def categoria_director_path(instance, filename):
    banner_pic_name = 'markepace/categorias/{0}/{1}'.format(instance.title, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return banner_pic_name
################################################################################################
#                                         #
#                MOSTRAR ITENS            #        MOSTRAR ITENS
#                                         #
#                                         #
################################################################################################
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    cat_image  = models.ImageField(blank=True, null=True, upload_to=categoria_director_path)

    class Meta:
        verbose_name_plural = 'Categories'

    @staticmethod
    def get_all_categories():
        return Category.objects.all() 
       
    def __str__(self):
        return self.title

    @property
    def imageURL(self):

        url = self.cat_image
        return url    

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
  
    # to save the data
    def register(self):
        self.save()
  
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
  
        return False
    
class Product(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    
    id = models.AutoField(
        primary_key=True,
        unique=True,
        )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=100)
    thunbnail = models.ImageField(blank=True, null=True, upload_to=marketplace_director_path)
    content_url = models.URLField(blank=True, null=True)
    content_file = models.FileField(blank=True, null=True)
    active = models.BooleanField(default=False)
    created_art = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_art", )    
    
    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):

        url = self.thunbnail
        return url
        
    def price_display(self):
        return "{0:.2f}".format(self.price / 1) 
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Product.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
  
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

class CartItem(models.Model): 
    cart_id = models.CharField(max_length=50) 
    date_added = models.DateTimeField(auto_now_add=True) 
    quantity = models.IntegerField(default=1) 
    product = models.ForeignKey(Product, unique=False,on_delete=models.CASCADE) 
 
    class Meta: 
        db_table = 'cart_items' 
        ordering = ['date_added'] 
    
    def total(self): 
        return self.quantity * self.product.price 
    
    def name(self): 
        return self.product.name 
    
    def price(self): 
        return self.product.price
    
    def get_absolute_url(self): 
        return self.product.get_absolute_url()
    
    def augment_quantity(self, quantity): 
        self.quantity = self.quantity + int(quantity)
        self.save()    
            

class PurchasedProducts(models.Model):
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email    
                   