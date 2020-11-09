import time
from django.urls import reverse
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,Http404
from django.contrib import messages
from django.utils import timezone
from .models import Item,customer,ItemOrder,CustomerOrder,Orders
from django.contrib.auth.models import User, auth

# Create your views here.
def about(request):
    return render(request,'about.html')

def index1(request):
    return render(request,'index1.html')

def menu(request):
    items = Item.objects.all()
    return render(request,'menu.html',{'items': items})


def signup(request):

    if request.method == 'POST':
        username = request.POST[ 'username']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       
        if password1==password2:
            if customer.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                post=customer()
                post.username=username
                post.phone=phone
                post.password=password1
                post.save()
                user=User.objects.create_user(username=username,password=password1)
                user.save()

                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('signup')

    else:
        return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('cusin')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
         return render(request,'login.html')


def customersignup(request):
    return render(request,'customer.html')

def cusin(request):
    return render(request,'cusin.html')

def menu2(request):
    
        products = Item.objects.all()
        return render(request,'menu2.html',{'products': products})
    


def gallery(request):
    return render(request,'gallery.html')

def restauraunt(request):
    return render(request,'restauraunt.html')

#def signup2(request):

  #  if request.method == 'POST':
   #     username = request.POST[ 'username']
    #    phone = request.POST['phone']
     #   password1 = request.POST['password1']
      #  password2 = request.POST['password2']
       
       # if password1==password2:
        #    if resta.objects.filter(username=username).exists():
          #      messages.info(request, 'Username taken')
          #      return redirect('signup2')
          #  else:
          #      post=resta()
           #     post.username=username
            #    post.phone=phone
             #   post.password=password1
              #  post.save()
               # user=User.objects.create_user(username=username,password=password1)
               # user.save()

                #return redirect('login2')
        #else:
         #   messages.info(request,'password not matching')
          #  return redirect('signup2')

    #else:
     #   return render(request,'signup2.html')

def login2(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if customer.objects.filter(role='1', username=username,password=password).exists():
            if user is not None:
                auth.login(request, user)
                return redirect('restin')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login2')

    else:
         return render(request,'login2.html')

def restin(request):
    return render(request,'restin.html')

def menu3(request):
    if request.method=='POST':
     name=request.POST['name']
     price=request.POST['price']
     #isActive=request.POST['isActive']

     instance=Item()
     instance.name=name
     instance.price=price
     #instance.isActive=isActive
     instance.save()
     
     return redirect('restin')
     
    else:
        return render(request,'menu3.html')

def deletee(request):
    items = Item.objects.all()
    return render(request,'deletee.html',{'items': items})
    
def delete(request ,id):
    items = Item.objects.get(id=id)
    items.delete()
    return redirect('deletee')
    



def contact(request):
    return render(request,'contact.html')

def logout(request):
    return redirect('/')
 
def logout2(request):
    return redirect('/')


def abc(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id=None
    if the_id:
        order = CustomerOrder.objects.get(id=the_id)
        if request.method == 'POST':
            address = request.POST['address']
            order.address = address
            order.save()
            return redirect('abc')

        context = {"order":order}
    else:
        empty_message = "It is Empty!!"
        context = {"empty": True, "empty_message": empty_message}

    template = "abc.html"
    return render(request,template,context)



def update_cart(request, slug):
    request.session.set_expiry(6048000)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = CustomerOrder()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    order = CustomerOrder.objects.get(id=the_id)
   # o = CustomerOrder()
    o1 = request.user
    order.userid = o1
    order.save()
    

    
    try:
        product = Item.objects.get(slug=slug)
    except Item.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = ItemOrder.objects.get_or_create(userid=o1,cart=order,product=product)

    if created:
        print("yeah")

    
    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else: 
            cart_item.quantity=qty
            cart_item.save()
    else:
        pass
    
    # if not cart_item in order.items1.all():
    #      order.items1.add(cart_item)
    # else:
    #      order.items1.remove(cart_item)

    new_total = 0.00
    for item in order.itemorder_set.all():
        line_total = float(item.product.price) *  item.quantity
        new_total += line_total

    order.total = new_total
    order.total=new_total
    order.save()
    order.save()
    return redirect('menu2')




# def update(request):
#     # order = ItemOrder.objects.get(id=cart)
#     # return render(request,'update.html',{'order': order})

#     try:
#         the_id = request.session['cart_id']
#     except:
#         the_id=None
#     if the_id:
#         order = CustomerOrder.objects.get(id=the_id)
#         context = {"order":order}
#     else:
#         empty_message = "It is Empty!!"
#         context = {"empty": True, "empty_message": empty_message}

#     template = "update.html"
#     return render(request,template,context)

def checkout(request):

    try:
        the_id = request.session['cart_id']
        cart = CustomerOrder.objects.get(id=the_id)
        
    except:
        the_id=None
        return HttpResponseRedirect(reverse("abc"))

    new_order, created = Orders.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = str(time.time())
        new_order.save()
        o1 = request.user
        new_order.userid = o1
        new_order.save()

    
    if new_order.setstatus == "delivered":
        cart.delete()
        del request.session['cart_id']
        return HttpResponseRedirect(reverse("abc"))



    ob = Orders.objects.all()
    context= {'ob':ob}
    template = "checkout.html"
    return render(request, template, context)



def orderlist(request):
    order = Orders.objects.all()
    return render(request,'orderlist.html',{'order': order})


def view(request, pk_test):
    ob = ItemOrder.objects.filter(cart=pk_test)
    order = CustomerOrder.objects.get(id=pk_test)
    return render(request,'view.html',{'ob':ob , 'order':order })




def setstatus(request,id):
    ob = Orders.objects.get(id=id)

    if request.method == 'POST':
        setstatus = request.POST['setstatus']
        ob.setstatus = setstatus
        ob.save()

    return redirect('orderlist')


def deleteorder(request,id):
    ob = Orders.objects.get(id=id)
    ob.delete()
    return redirect('orderlist')
    

def myorders(request):
    # order = Orders.objects.filter(userid=id)
    # return render(request,'myorders.html',{'order': order})
    try:
        # the_id = request.session['cart_id']
        o1 = request.user
    except:
        # the_id=None
        o1=None
    if  o1:
        order = Orders.objects.filter(userid=o1)
        

    template = "myorders.html"
    return render(request,template,{'order':order})


def myordersview(request, pk_test):
    ob = ItemOrder.objects.filter(cart=pk_test)
    order = CustomerOrder.objects.get(id=pk_test)

    return render(request,'myordersview.html',{'ob':ob , 'order':order })
