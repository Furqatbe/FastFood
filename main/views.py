from itertools import product
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import viewsets , filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from datetime  import datetime
import datetime

# Create your views here.

@api_view(['GET'])
def GetSlider(request):
    a = Slider.objects.all().order_by('-id')[0:3]
    ser = SliderSerializer(a , many= True)

    return Response(ser.data)

@api_view(['GET'])
def GetNews(request):
    a = News.objects.all().order_by('-id')[0:4]
    ser = NewsSerializer(a , many= True)

    return Response(ser.data)

@api_view(['GET'])
def GetInfo(request):
    a = Info.objects.last()
    ser = InfoSerializer(a)

    return Response(ser.data)


@api_view(['GET'])
def GetCategory(request):
    a = Category.objects.all()
    ser = CategorySerializer(a , many= True)

    return Response(ser.data)

@api_view(['GET'])
def GetProduct(request):
    a = Product.objects.all().order_by('-id')[0:10]
    ser = ProductSerializer(a , many= True)

    return Response(ser.data)

@api_view(['GET'])
def FlProduct(request):
    name = request.GET['name']
    a = Product.objects.filter(category__name = name )
    ser =ProductSerializer(a , many= True)

    return Response(ser.data)

@api_view(['GET'])
def FlProductName(request):
    name = request.GET['search']
    a= Product.objects.filter(name__icontains = name)
    ser = ProductSerializer(a , many= True)

    return Response(ser.data)

@api_view(['GET'])
def FlProductPrice(request):
    price = request.GET['price']
    a= Product.objects.filter(price__icontains = price)
    ser = ProductSerializer(a , many= True)

    return Response(ser.data)



@api_view(['POST'])
def Register(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.create_user(username='user-'+username)
    user.set_password(password)
    user.save()
    token = Token.objects.create(user=user)
    DATA = {
        "username":username,
        "password":user.password,
        "token":str(token)

    }
    return Response(DATA)



@api_view(['POST'])
def Login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.filter(username='user-'+username)
    if len(user)>0:
        if user[0].check_password(password) == True:
            token = Token.objects.get(user= user[0])
            DATA = {
                    "username":username,
                    "password":user[0].password,
                    "token":str(token)

                }
            return Response(DATA)
        else:
            return Response({"status" : "password xato"})
    else:
        return Response({"status" : "username xato"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Subscriber(request):
    email = request.POST.get('email')
    a = Subscriber.objects.create(email=email)
    ser = SubscriberSerializer(a)
    return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CreateCart(request):
    product = request.POST.get('product')
    user = request.user
    quantity = request.POST.get('quantity')
    product = Product.objects.get(id=product)
    a = Cart.objects.create( product =  product, user= user,  quantity=quantity, )
    ser = CartSerializer(a)
    return Response(ser.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def GetCart(request):
    user = request.user
    a= Cart.objects.filter(user = user)
    ser = CartSerializer(a , many= True)

    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def DeleteCart(request, pk):
    user = request.user
    a= Cart.objects.filter(user = user, id=pk)
    a.delete()
    data = {'status':"O'chirildi"}

    return Response(data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def UpdateCart(request, pk):
    user = request.user
    new_quantity = request.POST.get('quantity')
    cart = Cart.objects.get( user= user,  id=pk)
    cart.quantity = new_quantity
    cart.save()
    ser = CartSerializer(cart)

    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Order_Add(request):
    
    user = request.user
    cart = Cart.objects.filter(user=user)
    for c in cart:
        order = Order.objects.create(user=user, date=datetime.datetime.now(), totle_price = c.product.price*c.quantity)
        # order_item = OrderItem.objects.create(order=order, product=c.product, quantity=c.quantity)
        c.delete()
    orders = Order.objects.filter(user=user, order = order )
    ser = OrderSerializer(orders, many = True)
    return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CreateContacUs(request):
    user = request.user
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    number = request.POST.get('number')
    adress = request.POST.get('adress')
    a = ContactUs.objects.create(user=user,name=name, number=number, adress=adress, message=message, email=email )
    ser = ContactUsSerializer(a)
    return Response(ser.data)


