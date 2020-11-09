from django.contrib import admin
from .models import Item,customer,CustomerOrder,ItemOrder,Orders

 #Register your models here.
admin.site.register(Item)
admin.site.register(customer)
admin.site.register(CustomerOrder)
admin.site.register(ItemOrder)
admin.site.register(Orders)

