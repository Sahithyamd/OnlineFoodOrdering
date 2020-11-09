from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length=200)
   # desc = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    #isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("apps:detail", kwargs ={'slug':self.slug})

def create_slug(instance,new_slug = None):
    slug=slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Item.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver,Item)



class customer(models.Model):

    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=10 )
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=2,default='0')




class ItemOrder(models.Model):
    userid = models.ForeignKey(User,blank = True , null = True, default=None,on_delete=models.CASCADE)
    cart = models.ForeignKey('CustomerOrder', default=None,on_delete=models.CASCADE)
    product = models.ForeignKey(Item, default=None, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    #line_total = models.DecimalField(max_digits= 100, decimal_places=2, default=0.00)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.name


class CustomerOrder(models.Model):
    userid = models.ForeignKey(User,blank = True , null = True,default=None,on_delete=models.CASCADE)
    #status = models.TextField(max_length=100)
    #items1 = models.ManyToManyField(ItemOrder, null=True, blank=True)
    #products = models.ManyToManyField(Item, null=True,blank=True)
    createdon = models.DateField(default=datetime.now)
    address = models.TextField(max_length=100, blank=True)
    total = models.DecimalField(max_digits= 100, decimal_places=2, default=0.00)


class Orders(models.Model):
    userid = models.ForeignKey(User,blank = True , null = True,default=None,on_delete=models.CASCADE)

    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(CustomerOrder, default=None,on_delete=models.CASCADE)
    #status = models.CharField(max_length=120, choices = STATUS_CHOICES, default="pending")
    setstatus = models.CharField(max_length=50, default="Pending")

    def __unicode__(self):
        return self.order_id


