from django.urls import path
from . import views


urlpatterns = [
    path('about',views.about,name='about'),
    path('index1',views.index1,name='index1'),
    path('menu',views.menu,name='menu'),
    path('customersignup',views.customersignup,name='customersignup'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('cusin',views.cusin,name='cusin'),
    path('menu2',views.menu2,name='menu2'),

    path('gallery',views.gallery,name='gallery'),
    path('restauraunt',views.restauraunt,name='restauraunt'),
    # path('signup2',views.signup2,name='signup2'),
    path('login2',views.login2,name='login2'),
    path('restin',views.restin,name='restin'),
    path('menu3',views.menu3,name='menu3'),
    path('deletee',views.deletee,name='deletee'),
    path('delete/<int:id>',views.delete,name='delete'),


    path('contact',views.contact,name='contact'),
    path('logout',views.logout,name='logout'),
    path('logout2',views.logout2,name='logout2'),
    path('abc',views.abc,name='abc'),
    path('update_cart/<slug:slug>',views.update_cart,name='update_cart'),
    path('checkout',views.checkout, name='checkout'),
    path('orderlist',views.orderlist,name='orderlist'),
    path('view/<int:pk_test>',views.view,name='view'),
    path('setstatus/<int:id>',views.setstatus, name='setstatus'),
    path('deleteorder/<int:id>',views.deleteorder,name='deleteorder'),
    path('myorders',views.myorders,name='myorders'),
    path('myordersview/<int:pk_test>',views.myordersview,name='myordersview'),


 


    
    ]