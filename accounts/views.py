from django.shortcuts import render, HttpResponseRedirect
from .models import *
from ecommerce.models import Product
from django.contrib.auth.decorators import login_required
from ecommerce.views import *
from carts.views import *
from django.urls import reverse
from django.contrib.sessions.models import Session
from .forms import * 
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
import time
from django.contrib.auth.models import User
from orders.views import *
from carts.views import *
from accounts.models import * 

def add_address(request):
    request.session.set_expiry(120000)
    # Get the back page
    try: 
        next_page = request.GET.get("next")
    except:
        next_page= None
    
    try: 
        address = UserDefaultAddress.objects.get(user=request.user)
        context={'address' : address}
    except:
        context={}
        pass

    # Input the new address
    if request.method == 'POST':
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        phone_number = request.POST['phone_number']
        billing = 'billing' in request.POST
        
        if UserAddress.objects.filter(user=request.user, address=address).exists():
            messages.info(request, 'Your address existed in your account')
        else:
            new_address = UserAddress.objects.create(user=request.user, address=address, city = city, state=state, zipcode=zipcode, phone_number=phone_number, billing=billing)
            new_address.save()
            messages.success(request, 'Saved a new address successfully')

        # Check the billing, if billing is true, that means the customer wants to change the default address, so replace the default address
        if billing == True: 
            try: 
                addressDefault = UserDefaultAddress.objects.get(user=request.user)
                addressDefault.delete()
                address1 = UserAddress.objects.filter(user=request.user, billing=True)[0]
                address1.billing = False
                address1.save()
                address2 = UserAddress.objects.get(user=request.user, billing=True)
                default_address = UserDefaultAddress.objects.create(user=request.user,shipping=address)  
            except UserAddress.objects.get(user=request.user, billing=True).exist(): 
                address3 = UserAddress.objects.get(user=request.user, billing=True)
                default_address = UserDefaultAddress.objects.create(user=request.user,shipping=address3)  
            except: 
                messages.info(request, 'No default address')
                pass
        
    # Get back to the page
        if next_page is not None: 
            return HttpResponseRedirect(reverse(next_page)+"?address_added=True")
        else: 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    template = 'accounts/newaddress.html'
    return render(request, template, context)


def profile(request):
    request.session.set_expiry(120000)
    user = request.user
    try: 
        next_page = request.GET.get("next")
    except:
        next_page= None

    if request.method == 'POST': 
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
        else: 
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                if next_page is not None: 
                    return HttpResponseRedirect(reverse(next_page)+"?address_added=True")
                else: 
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request,'accounts/newaddress.html')

# def defaultAddress(request):
#     address = UserAddress.objects.filter(user=request.user)
#     if request.method == 'POST': 
#         default = request.POST['shipping']
#         new_default = UserAddress.objects.get(user=request.user, id=default)
#         new_default.billing = True
#         new_default.save()

#         address = UserAddress.objects.get(user = request.user, billing=True)
#         default_address = UserDefaultAddress.objects.create(user=request.user,shipping=address)  
#         default_address.save()
#         return redirect(cart)
#     context = {"address": address }
#     return render(request,'accounts/newaddress1.html', context)
